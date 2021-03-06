from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from ams import models
from ams.forms import StaffForm
from ams.models import Staff


class Add(LoginRequiredMixin, generic.CreateView):
    form_class = StaffForm
    success_url = reverse_lazy('ams:staff-list')
    template_name = 'ams/staff/_staff_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class List(LoginRequiredMixin, generic.ListView):
    model = Staff
    template_name = 'ams/staff/staff.html'
    paginate_by = 10
    queryset = Staff.objects.filter(deleted=False)
    context_object_name = 'staffs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lead'] = models.DepartmentLead.objects.all()
        context['department'] = models.Allocation.objects.all()
        return context


class ArchiveList(LoginRequiredMixin, generic.ListView):
    model = Staff
    template_name = 'ams/staff/staff-archives.html'
    paginate_by = 10
    queryset = Staff.objects.filter(deleted=True)
    context_object_name = 'staff_archives'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = models.Allocation.objects.all()
        return context


class NewList(LoginRequiredMixin, generic.ListView):
    model = Staff
    template_name = 'ams/staff/staff-archives.html'

    def get_queryset(self):
        return Staff.objects.filter(deleted=True)


class Detail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/staff/details-staff.html'
    model = models.InformationAssign

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['information'] = models.InformationAssign.objects.all()
        context['infrastructure'] = models.InfrastructureAssign.objects.all()
        context['hardware'] = models.HardwareAssign.objects.all()
        context['software'] = models.SoftwareAssign.objects.all()
        context['department'] = models.Allocation.objects.all()
        return context

    def get_queryset(self):
        return Staff.objects.all()


class ArchiveDetail(LoginRequiredMixin, generic.DetailView):
    template_name = 'ams/staff/staff-archive-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = models.Allocation.objects.all()
        return context

    def get_queryset(self):
        return Staff.objects.all()


class Update(LoginRequiredMixin, generic.UpdateView):
    form_class = StaffForm
    template_name = 'ams/staff/update-staff.html'
    success_url = reverse_lazy('ams:staff-list')

    def get_queryset(self):
        return Staff.objects.all()


class Archive(LoginRequiredMixin, generic.DeleteView):
    model = Staff
    success_url = reverse_lazy('ams:staff-list')
    # template_name = 'ams/assets/details-hardware.html'

    def get_queryset(self):
        return Staff.objects.filter()


class Restore(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:staff-list')
    model = Staff
    fields = ['deleted', ]

    def get_queryset(self):
        return Staff.objects.filter()
