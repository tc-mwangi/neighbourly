from django import forms
from .models import Hood, Profile, Business, locations


class EditProfileForm(forms.Form):
    class Meta:
        model= Profile
        exclude =['user']


class ChangeHoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ['']    


class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['']


class PostForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['']



        





