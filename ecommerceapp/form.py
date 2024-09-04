from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import items

class creatuserform(UserCreationForm):
    class  Meta:
        model = User
        fields = ('username' , 'email','password1','password2')

class loginuserform(AuthenticationForm):
    class  Meta:
        model = User
        fields = ('username' ,'password')

