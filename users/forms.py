from django import forms
from django.contrib.auth.models import User
from users import models


class LogoutForm(forms.Form):
    pass


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. Victor'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. Victor'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'eg. email@example.com'}))

    class Meta:
        model = models.UserProfile
        fields = ('first_name', 'last_name', 'email')
