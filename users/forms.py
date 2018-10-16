from django import forms

from users import models


class LogoutForm(forms.Form):
    pass


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = models.UserProfile
        fields = ('first_name', 'last_name', 'email')
