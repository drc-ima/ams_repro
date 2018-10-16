from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain

from ams import models
from django.views import generic


class List(LoginRequiredMixin, generic.ListView):
    template_name = 'ams/assets/owner/owner.html'
    model = models.HardwareOwner

    def get_context_data(self, **kwargs):
        software = models.SoftwareOwner.objects.all()
        hardware = models.HardwareOwner.objects.all()
        information = models.InformationOwner.objects.all()
        infrastructure = models.InfrastructureOwner.objects.all()
        owner_list = chain(software, hardware, information, infrastructure)
        context = super().get_context_data(**kwargs)
        context['owner_list'] = owner_list
        return context
