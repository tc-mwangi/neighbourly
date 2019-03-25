from django import forms
from .models import Hood, Profile, Business, Join, Post


class EditProfileForm(forms.Form):
    class Meta:
        model= Profile
        exclude =['user']


class ChangeHoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ['member', 'user_profile', 'profile', ]    


class PostForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['']

    exclude = ['author', 'post_hood']


class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['business_owner', 'business_hood']





        





