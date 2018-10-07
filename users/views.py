from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from users import forms
# from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic


class SignupView(LoginRequiredMixin, generic.CreateView):
    form_class = UserCreationForm
    template_name = 'ams/settings/setting.html'
    success_url = reverse_lazy('ams:settings')


class PasswordChangeView(LoginRequiredMixin, generic.FormView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('ams:department-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['users'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the users
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class CreateProfile(LoginRequiredMixin, generic.CreateView):
    form_class = forms.UserProfileForm
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
