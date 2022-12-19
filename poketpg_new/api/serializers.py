from rest_framework import serializers
from .models import User,owner,hostler

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= User
#         fields= ['id','username','password','email']


class dataSerializer1(serializers.ModelSerializer):
    class Meta:
        model= owner
        fields= ['id','name','email','companyname','password','location']


class dataSerializer2(serializers.ModelSerializer):
    class Meta:
        model= hostler
        fields= ['id','name','age','address','email','college','password','phno','location']


