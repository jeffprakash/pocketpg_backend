from imaplib import _Authenticator
from xmlrpc.client import ResponseError
from django.shortcuts import render
from .serializers import dataSerializer1,dataSerializer2
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets ,permissions
from django.contrib import auth
from .models import User,owner,hostler
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import dataSerializer1
from rest_framework import viewsets
from rest_framework.response import Response



# Create your views here.
@api_view(['GET'])
def get_owner_details(request):                                          #api to get details of owner
    users=owner.objects.all()
    serializer =dataSerializer1(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_hostler_list(request):
    users=hostler.objects.all()                                        #api to get all hostler
    serializer =dataSerializer2(users, many=True)
    return Response(serializer.data)

class signup_owner(APIView):
    def post(self, request):                                             #signup for owner


    # serializer= dataSerializer1(data=request.data)
    # if serializer.is_valid():
    #      user_id = serializer.validated_data.get('user_id')
    #      #user_exists=User.objects.get(username=username)
         
    #      serializer.save()
         
    #      return Response({"signup":"success"})
    # else:
    #     return Response(serializer.errors)

       serializer = dataSerializer1(data=request.data)
       if serializer.is_valid():
            # Create a new user
            # user = dataSerializer1.objects.create_user(
            #     name=serializer.data['name'],
            #     email=serializer.data['email'],
            #     companyname=serializer.data['companyname'],
            #     password=serializer.data['password'],
            #     location=serializer.data['location']
               
            # )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_owner_by_num(request,pk):                              #api to get owner list by id
    num=owner.objects.get(id=pk)
    serializer = dataSerializer1(num,many=False)
   
   
    return Response(serializer.data)


@api_view(['GET'])
def get_hostler_by_num(request,pk):                              #api to get hostler list by id
    num=hostler.objects.get(id=pk)
    serializer =dataSerializer2(num,many=False)
    return Response(serializer.data)

# @api_view(['POST'])
# def form(request):
#     serializer= dataSerializer(data=request.data)
#     if serializer.is_valid():
#          user_id = serializer.validated_data.get('user_id')
#          #user_exists=User.objects.get(username=username)
         
#          serializer.save()
         
#          return Response({"data":"added"})
#     else:
#         return Response(serializer.errors)


class signup_hostler(APIView):
    def post(self, request):                                                #signup for  hostler
                                                                    

        serializer = dataSerializer2(data=request.data)
        if serializer.is_valid():
            # Create a new user
            # user = dataSerializer2.objects.create_user(
            #     username=serializer.data['name'],
            #     age=serializer.data['age'],                                   
            #     address=serializer.data['address'],
            #     email=serializer.data['email'],
            #     college=serializer.data['college'],
            #     password=serializer.data['password'],
            #     phno=serializer.data['phno'],
            #     location=serializer.data['location']
                
            # )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)         #status not giving
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ownerdetail(APIView):
#     """
#     Retrieve, update or delete a transformer instance
#     """
#     def get_object(self, pk):
#         # Returns an object instance that should 
#         # be used for detail views.
#         try:
#             return .objects.get(pk=pk)
#         except Transformer.DoesNotExist:
#             raise Http404