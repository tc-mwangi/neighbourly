from django.db import models
import datetime as datetime
from django import forms
from django.contrib.auth.models import User
from tinymce.models import HTMLField




# locations = (
#     ('Karen', 'Karen'),
#     ('Kikuyu', 'Kikuyu'),
#     ('Ngong', 'Ngong'),
#     ('Limuru', 'Limuru'),
# )


class Hood(models.Model):
    '''creates instances of neighbourhoods
    
    Arguments:
        models {[type]} -- [description]
    '''
    name = models.CharField(max_length=50, blank=True)
    # location = models.CharField(max_length=6, choices= locations, blank=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    member_count = models.IntegerField(default=0, null=True)
    police_details = HTMLField(blank=True)
    health_details = HTMLField(blank=True)



    def __str__(self):
        return self.name

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    
    @classmethod
    def find_a_hood(hood_id):
        hood = Hood.objects.filter(id=hood_id)
        return hood

    @classmethod
    def get_all_occupants(cls):
        occupants= cls.objects.get_all()
        return occupants

    @classmethod
    def search_neighborhood_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    @classmethod
    def hood_by_id(cls, id):
        hood = Hood.objects.filter(id=id)
        return hood

    @classmethod
    def get_all_hoods(cls):
        hood = cls.objects.all()
        return hood

    @classmethod
    def get_neighborhood_by_id(cls, id):
        hood = Hood.objects.filter(id=Hood.id)
        return hood

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile


class Business(models.Model):
    name = models.CharField(max_length=30)
    description = HTMLField(blank=True)
    email = models.EmailField(max_length=70, blank=True)
    business_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    business_hood = models.ForeignKey(
    Hood, on_delete=models.CASCADE, related_name='business', null=True)

    objects = models.Manager()

    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    @classmethod
    def get_neighborhood_business(cls, hood_id):
        business = Business.objects.filter(hood_id=id)
        return business

    @classmethod
    def get_hood_business(cls, business_hood):
        business = Business.objects.filter(business_hood_pk=biz_hood)
        return business

    @classmethod
    def get_profile_business(cls, profile):
        business = Business.objects.filter(biz_owner__pk=profile)
        return business


class UpdateHood(models.Model):
    '''updates user location
    
    Arguments:
        models {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    user_id = models.OneToOneField(User)
    hood_id = models.ForeignKey(Hood)

    def __str__(self):
        return self.user_id



class Profile(models.Model):
    '''creates instances of user profiles
    
    Arguments:
        models {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    avatar = models.ImageField(upload_to='avatar/', null=True)
    bio = models.TextField(max_length=255)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=100, blank=True)


    def __str__(self):
        return self.user

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
    post_hood = models.ForeignKey(Hood, on_delete=models.CASCADE, null=True)
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



    


