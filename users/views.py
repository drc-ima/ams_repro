from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render

from users import forms
# from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic


class SignupView(LoginRequiredMixin, generic.CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('ams:settings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateProfile(LoginRequiredMixin, generic.CreateView):
    form_class = forms.UserProfileForm
    template_name = 'ams/settings/_profile.html'
    success_url = reverse_lazy('ams:settings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('ams:settings')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password_change.html', {
        'form': form
    })
