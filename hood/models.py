from django.db import models
import datetime as datetime
from django import forms
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Admin(models.Model):
    '''creates instances of neighbourhood locations
    
    Arguments:
        models {[type]} -- [description]
    '''

    name = models.CharField(max_length=50)


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


class Hood(models.Model):
    '''creates instances of neighbourhoods
    
    Arguments:
        models {[type]} -- [description]
    '''
    name = models.CharField(max_length=50, null=True)
    location = models.ForeignKey(locations, null=True)
    occupant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    police_details = models.ForeignKey(Police)
    health_details = models.ForeignKey(Health)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name

    def create_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    def update_hood(self):
        self.update()

    
    @classmethod
    def find_hood(hood_id):
        hood = Hood.objects.filter(id=hood_id)
        return hood

    @classmethod
    def update_occupants(cls):
        occupants= cls.objects.get_all()
        return occupants


    


class Profile(models.Model):
    '''creates instances of user profiles
    
    Arguments:
        models {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    occupant = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
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







class Business(models.Model):
    '''creates instances of businesses listed in a neighbourhood
    
    Arguments:
        models {[type]} -- [description]
    '''
    name = models.CharField(max_length=50, null=True)
    hood = models.ForeignKey(Hood, null=True)
    occupant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
   


    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    
    @classmethod
    def search_business(cls,business_id):
        business= cls.objects.filter(id=business_id)
        return business
        


    @classmethod
    def update_business(cls):
        occupants= cls.objects.get_all()
        return occupants


# indicate which models should be shared
# class Pin(Activity, models.Model):
    


