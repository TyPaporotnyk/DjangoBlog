from django import forms
from django.contrib.auth import (authenticate, get_user_model,
                                 password_validation)
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import widgets

from .models import Account


class AccountAuthenticationForm(forms.ModelForm):
    """User Account Form 
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('nickname', 'password')
	
    def clean(self):
        if self.is_valid():
            nickname = self.cleaned_data['nickname']
            password = self.cleaned_data['password']
        if not authenticate(nickname=nickname, password=password):
            raise forms.ValidationError("Invalid login")
        

class AccountRegisterForm(UserCreationForm):
    """User Account creation form
    """
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email):
            raise ValidationError("User with this email is already exist")
        return email

    def clean_nickname(self):
        nickname = self.cleaned_data["nickname"]
        if get_user_model().objects.filter(nickname=nickname):
            raise ValidationError("User with this nickname is already exist")
        return nickname

    class Meta:
        model = get_user_model()
        fields = ('email', 'nickname', 'password1', 'password2', )


class AccountChangeForm(UserChangeForm):
    """User Account Change form
    """
    pass
        