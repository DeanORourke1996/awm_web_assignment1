from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Users


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['user']


class UserLoginForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.PasswordInput()

    class Meta:
        model = Users
        fields = ['email', 'password1']
