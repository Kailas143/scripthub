from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MovieSearch

class MovieSearchForm(forms.ModelForm):
    name_of_movie=forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        'class':'form-control me-2','placeholder':'Enter Movie Title'
    }))
    class Meta:
       model=MovieSearch
       fields='__all__'




class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={
        'class' : 'form-control', 'placeholder': 'Enter Username'
    }))

    email=forms.CharField(max_length=100, required=False,widget=forms.EmailInput(attrs={
        'class':'form-control','placeholder':'Enter Email'
    }))
    password=forms.CharField(max_length=100, required=True,widget=forms.PasswordInput(attrs={
        'class':'form-contol','placeholder':'Enter Password'
    }))
    password1=forms.CharField(max_length=100, required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control','placeholder':'Confirm Password'
    }))
    
    class Meta:
        model = User
        fields=['username','email','password','password1',]