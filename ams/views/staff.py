from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staffs'] = Staff.objects.filter(dele_ted=False)
        context['archive_staff'] = Staff.objects.filter(dele_ted=True)
        return context


class Detail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/staff/details-staff.html'

    def get_queryset(self):
        return Staff.objects.all()


class ArchiveDetail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/staff/staff-archives.html'

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
        return Staff.objects.delete()


class Restore(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:staff-list')
    model = Staff

    def get_queryset(self):
        return Staff.objects.undelete()
