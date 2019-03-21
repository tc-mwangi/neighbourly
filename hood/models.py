from django.db import models
import datetime as datetime
from django import forms
from django.contrib.auth.models import User, Admin
from tinymce.models import HTMLField


class locations(models.Model):
    '''creates instances of neighbourhood locations
    
    Arguments:
        models {[type]} -- [description]
    '''

    name = models.CharField(max_length=50)


class Police(models.Model):
    '''creates instances of neighbourhood locations
    
    Arguments:
        models {[type]} -- [description]
    '''

    name = models.CharField(max_length=50)


class Health(models.Model):
    '''creates instances of neighbourhood locations
    
    Arguments:
        models {[type]} -- [description]
    '''

    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    box = models.TextField()
    


class Profile(models.Model):
    '''creates instances of user profiles
    
    Arguments:
        models {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    username = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    avatar = models.ImageField(upload_to='avatar/', null=True)
    bio = models.TextField(max_length=255)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, null=True)
    email = models.EmailField()


    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete__profile(self):
        self.delete()

    @classmethod
    def get_user_profile(cls,user_id):
        user_profile = cls.objects.filter(user=user_id)
        return user_profile





class Hood(models.Model):
    '''creates instances of neighbourhoods
    
    Arguments:
        models {[type]} -- [description]
    '''
    name = models.CharField(max_length=50, null=True)
    location = models.OnetoManyField(locations, null=True)
    occupants = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    police_details = models.ForeignKey(Police)
    health_details = models.ForeignKey(Health)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name

    def create_neighbourhood






class Profile(models.Model):




class Business(models.Model):