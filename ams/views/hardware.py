from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from ams import models, forms
from ..forms import HardwareForm
from django.views import generic


class Add(LoginRequiredMixin, generic.CreateView):
    form_class = HardwareForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/hardware/_hardware_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


"""
class List(LoginRequiredMixin, generic.ListView):
    model = Hardware
    template_name = 'ams/assets/hardware/hardware.html'

    def get_queryset(self):
        return Hardware.objects.filter(deleted=False)



class ArchiveList(LoginRequiredMixin, generic.ListView):
    model = Hardware
    template_name = 'ams/assets/hardware/hardware-archives.html'

    def get_queryset(self):
        return Hardware.objects.filter(dele_ted=True)
"""


class Detail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/hardware/details-hardware.html'

    def get_queryset(self):
        return models.Hardware.objects.all()


class Update(LoginRequiredMixin, generic.UpdateView):
    form_class = HardwareForm
    template_name = 'ams/assets/hardware/update-hardware.html'
    success_url = reverse_lazy('ams:assets-list')

    def get_queryset(self):
        return models.Hardware.objects.all()


class Archive(LoginRequiredMixin, generic.DeleteView):
    model = models
    success_url = reverse_lazy('ams:assets-list')
    # template_name = 'ams/assets/details-hardware.html'

    def get_queryset(self):
        return models.Hardware.objects.filter()


class Assign(LoginRequiredMixin, generic.CreateView):
    form_class = forms.HardwareAssignForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/assign/_hardware_assign.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Restore(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:assets-list')
    model = models.Hardware
    fields = ['deleted', ]

    def get_queryset(self):
        return models.Hardware.objects.filter()
