from django import forms
from .models import Hood, Profile, Business


class ProfileForm(forms.Form):
    your_name =forms.CharField(label='First Name', max_length=30)
    email=forms.EmailField(label='Email')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


