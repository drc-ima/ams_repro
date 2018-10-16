from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain

from ams import models
from django.views import generic


class List(LoginRequiredMixin, generic.ListView):
    template_name = 'ams/assets/assign/assign.html'
    model = models.HardwareAssign

    def get_context_data(self, **kwargs):
        software = models.SoftwareAssign.objects.all()
        hardware = models.HardwareAssign.objects.filter(approve=True)
        information = models.InformationAssign.objects.all()
        infrastructure = models.InfrastructureAssign.objects.all()
        assign_list = chain(software, hardware, information, infrastructure)
        context = super().get_context_data(**kwargs)
        context['assign_list'] = assign_list
        context['hardware'] = models.HardwareAssign.objects.filter(approve=False)
        return context


class ApproveDetail(LoginRequiredMixin, generic.DetailView):
    template_name = 'ams/assets/hardware/approve.html'

    def get_queryset(self):
        return models.HardwareAssign.objects.all()


class Detail(LoginRequiredMixin, SelectRelatedMixin, generic.DetailView):
    model = 'user'
    select_related = ('hardware_assign_by',)
    template_name = 'ams/assets/assign/assign.html'

    def get_object(self, queryset=None):
        return self.request.user
