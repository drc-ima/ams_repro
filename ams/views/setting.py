from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic


class Details(LoginRequiredMixin, SelectRelatedMixin, generic.ListView):
    model = 'user'
    select_related = ('profile', )
    template_name = 'ams/settings/setting.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_queryset(self):
        return User.objects.all()


class AllUsers(LoginRequiredMixin, generic.DetailView):
    template_name = 'ams/settings/setting.html'

    def get_queryset(self):
        return User.objects.all()
