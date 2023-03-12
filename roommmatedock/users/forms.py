from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User 

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class':'form-field', 'type':'password', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class':'form-field', 'type':'password', 'placeholder': 'Confirm Password'}),
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-field', 'placeholder': 'Email'}),
        }
