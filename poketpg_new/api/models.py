from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User=get_user_model()

class owner(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField(blank=False)
    email = models.EmailField(blank=True,null=True)
    companyname= models.TextField(blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)
    location=models.CharField(max_length=100,blank=True,null=True)
    


    def __str__(self):
        return self.name


class hostler(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField(blank=False)
    age  = models.IntegerField(blank=True,null=True)
    address= models.TextField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    college = models.TextField(blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)
    phno = models.IntegerField(blank=True,null=True)
    location=models.CharField(max_length=100,blank=True,null=True)
    
    


    def __str__(self):
        return self.name