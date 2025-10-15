from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']
        help_texts = {
            'username': None,
        }

class Loginform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)
