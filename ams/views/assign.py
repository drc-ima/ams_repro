from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain

from ams import models
from django.views import generic


class List(LoginRequiredMixin, generic.ListView):
    template_name = 'ams/assets/assign/assign.html'
    model = models.HardwareAssign

    def get_context_data(self, **kwargs):
        software = models.SoftwareAssign.objects.filter(approve=True)
        hardware = models.HardwareAssign.objects.filter(approve=True)
        information = models.InformationAssign.objects.filter(approve=True)
        infrastructure = models.InfrastructureAssign.objects.filter(approve=True)
        assign_list = chain(software, hardware, information, infrastructure)
        context = super().get_context_data(**kwargs)
        context['assign_list'] = assign_list
        return context


class ApproveList(LoginRequiredMixin, generic.ListView):
    template_name = 'ams/assets/assign/approve.html'
    model = models.HardwareAssign

    def get_context_data(self, **kwargs):
        software = models.SoftwareAssign.objects.filter(approve=False)
        hardware = models.HardwareAssign.objects.filter(approve=False)
        information = models.InformationAssign.objects.filter(approve=False)
        infrastructure = models.InfrastructureAssign.objects.filter(approve=False)
        approve_list = chain(software, hardware, information, infrastructure)
        context = super().get_context_data(**kwargs)
        context['approve_list'] = approve_list
        context['hardware'] = models.HardwareAssign.objects.filter(approve=False)
        context['software'] = models.SoftwareAssign.objects.filter(approve=False)
        context['information'] = models.InformationAssign.objects.filter(approve=False)
        context['infrastructure'] = models.InfrastructureAssign.objects.filter(approve=False)
        return context
