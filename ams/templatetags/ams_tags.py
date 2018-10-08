from django import template
# from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
# from django.utils import timezone
# import datetime
# import json
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

from ams import forms
from ams.forms import HardwareForm, SoftwareForm, InformationForm, InfrastructureForm, StaffForm, DepartmentForm, DepartmentLeadForm
from users.forms import UserProfileForm

register = template.Library()


@register.inclusion_tag('ams/assets/hardware/_hardware_form.html')
def hardware_form():
    form = HardwareForm
    return {'form': form}


@register.inclusion_tag('ams/assets/software/_software_form.html')
def software_form():
    form = SoftwareForm
    return {'form': form}


@register.inclusion_tag('ams/assets/information/_information_form.html')
def information_form():
    form = InformationForm
    return {'form': form}


@register.inclusion_tag('ams/assets/infrastructure/_infrastructure_form.html')
def infrastructure_form():
    form = InfrastructureForm
    return {'form': form}


@register.inclusion_tag('ams/staff/_staff_form.html')
def staff_form():
    form = StaffForm
    return {'form': form}


@register.inclusion_tag('ams/department/_department_form.html')
def department_form():
    form = DepartmentForm
    return {'form': form}


@register.inclusion_tag('registration/password_change.html')
def password_change_form():
    form = PasswordChangeForm
    return {'form': form}


@register.inclusion_tag('users/signup.html')
def signup_form():
    form = UserCreationForm
    return {'form': form}


@register.inclusion_tag('ams/assets/assign/_hardware_assign.html')
def hardware_assign_form():
    form = forms.HardwareAssignForm
    return {'form': form}


@register.inclusion_tag('ams/assets/asset_temp.html')
def information_assign_form():
    form = forms.InformationAssignForm
    return {'form': form}


@register.inclusion_tag('ams/assets/asset_temp.html')
def infrastructure_assign_form():
    form = forms.InfrastructureAssignForm
    return {'form': form}


@register.inclusion_tag('ams/assets/asset_temp.html')
def software_assign_form():
    form = forms.SoftwareAssignForm
    return {'form': form}


@register.inclusion_tag('ams/settings/_profile.html')
def profile_form():
    form = UserProfileForm
    return {'form': form}


@register.inclusion_tag('ams/department/_lead_form.html')
def lead_form():
    form = DepartmentLeadForm
    return {'form': form}