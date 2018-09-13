from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic


class Details(LoginRequiredMixin, generic.TemplateView):
    template_name = 'ams/settings/setting.html'
