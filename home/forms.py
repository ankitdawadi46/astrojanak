
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    fname=forms.CharField(max_length=30)
    lname=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    phone_number = forms.CharField()

    class Meta:
        model=User
        fields=["fname","lname","username","email","phone_number","password1","password2"]


