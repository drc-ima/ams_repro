from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain

from ams import models
from django.views import generic


class List(LoginRequiredMixin, generic.ListView):
    template_name = 'ams/assets/assets.html'
    model = models.Hardware

    def get_context_data(self, **kwargs):
        software = models.Software.objects.filter(deleted=False)
        hardware = models.Hardware.objects.filter(deleted=False)
        information = models.Information.objects.filter(deleted=False)
        infrastructure = models.Infrastructure.objects.filter(deleted=False)
        assets_list = chain(software, hardware, information, infrastructure)
        context_data = super().get_context_data(**kwargs)
        context_data['assets'] = assets_list
        context_data['software'] = models.Software.objects.filter(deleted=False)
        context_data['hardware'] = models.Hardware.objects.filter(deleted=False)
        context_data['information'] = models.Information.objects.filter(deleted=False)
        context_data['infrastructure'] = models.Infrastructure.objects.filter(deleted=False)
        software_a = models.Software.objects.filter(deleted=True)
        hardware_a = models.Hardware.objects.filter(deleted=True)
        information_a = models.Information.objects.filter(deleted=True)
        infrastructure_a = models.Infrastructure.objects.filter(deleted=True)
        archive_list = chain(software_a, hardware_a, information_a, infrastructure_a)
        context_data['archives'] = archive_list
        return context_data

"""
class Assign(LoginRequiredMixin, generic.CreateView):
    template_name = 'ams/assets/asset_temp.html'
    form_class = AssignForm
    success_url = reverse_lazy('ams:assets-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
"""

"""
class Archive(LoginRequiredMixin, generic.DeleteView):
    model = Assets
    success_url = reverse_lazy('ams:assets-list')
    # template_name = 'ams/assets/details-hardware.html'

    def get_queryset(self):
        return Assets.objects.filter()
"""


