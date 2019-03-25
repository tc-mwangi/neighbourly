from django.db import models
import datetime as datetime
from django import forms
from django.contrib.auth.models import User
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

    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    avatar = models.ImageField(upload_to='avatar/', null=True)
    bio = models.TextField(max_length=255)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=100, blank=True)


    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete__profile(self):
        self.delete()

    @classmethod
    def get_user_profile(cls,id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_a_profile(cls, search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    class Meta:
        ordering = ['user']


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



class Post(models.Model):
    '''create post instances
    
    Arguments:
        models {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)
    content = HTMLField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_hood = models.ForeignKey(
        Hood, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)


    @classmethod
    def get_hood_posts(cls, post_hood):
        posts = Post.objects.filter(post_hood=id)
        return posts

    @classmethod
    def search_post(cls, search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts  

    @classmethod
    def search_by_name(cls, search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts

    @classmethod
    def get_all_posts(cls,id):
        posts = Post.objects.all()
        return posts



    


