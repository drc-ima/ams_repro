from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy

from ams import models, forms
from ams.models import Hardware
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
"""


class ArchiveList(LoginRequiredMixin, generic.ListView):
    model = Hardware
    template_name = 'ams/assets/hardware/hardware-archives.html'

    def get_queryset(self):
        return Hardware.objects.filter(deleted=True)


class ArchiveDetail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/hardware/hardware-archive-detail.html'

    def get_queryset(self):
        return Hardware.objects.all()


class Detail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/hardware/details-hardware.html'

    def get_queryset(self):
        return models.Hardware.objects.all()


class ApproveDetail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/hardware/approve-details-hardware.html'

    def get_queryset(self):
        return models.HardwareAssign.objects.all()


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
    model = models.HardwareAssign
    form_class = forms.HardwareAssignForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/assign/_hardware_assign.html'

    def form_valid(self, form):
        form.instance.assign_by = self.request.user
        return super(Assign, self).form_valid(form)


class Approve(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:assign-list')
    form_class = forms.HardwareApproveForm
    # fields = ['approve', ]
    template_name = 'ams/assets/hardware/approve-details-hardware.html'

    def get_queryset(self):
        return models.HardwareAssign.objects.filter()


class Owner(LoginRequiredMixin, generic.CreateView):
    form_class = forms.HardwareOwnerForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/owner/_hardware_owner.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Restore(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:assets-list')
    model = models.Hardware
    fields = ['deleted', ]

    def get_queryset(self):
        return models.Hardware.objects.filter()


class Delete(LoginRequiredMixin, generic.DeleteView):
    model = models
    success_url = reverse_lazy('ams:assets-list')

    # template_name = 'ams/assets/details-hardware.html'

    def get_queryset(self):
        return models.Hardware.objects.hard_delete()


def approval(request):
    approve = request.GET.get('approve', False)
    hardware_slug = request.GET.get('hardwareassign_slug', False)
    # first you get your Job model
    hardware = models.HardwareAssign.objects.get(slug=hardware_slug)
    try:
        hardware.active = approve
        hardware.save()
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False})
    return JsonResponse(data)
