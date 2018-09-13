from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import Assets, Hardware
from ..forms import HardwareForm
from django.views import generic


class Add(LoginRequiredMixin, generic.CreateView):
    form_class = HardwareForm
    success_url = reverse_lazy('ams:assets-hardware-list')
    template_name = 'ams/assets/hardware/_hardware_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class List(LoginRequiredMixin, generic.ListView):
    model = Hardware
    template_name = 'ams/assets/hardware/hardware.html'

    def get_queryset(self):
        return Hardware.objects.filter(deleted=False)


class ArchiveList(LoginRequiredMixin, generic.ListView):
    model = Hardware
    template_name = 'ams/assets/hardware/hardware-archives.html'

    def get_queryset(self):
        return Hardware.objects.filter(deleted=True)


class Detail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/hardware/details-hardware.html'

    def get_queryset(self):
        return Hardware.objects.all()


class Update(LoginRequiredMixin, generic.UpdateView):
    form_class = HardwareForm
    template_name = 'ams/assets/hardware/update-hardware.html'
    success_url = reverse_lazy('ams:assets-hardware-list')

    def get_queryset(self):
        return Hardware.objects.all()


class Delete(LoginRequiredMixin, generic.DeleteView):
    model = Hardware
    success_url = reverse_lazy('ams:assets-hardware-list')
    # template_name = 'ams/assets/details-hardware.html'

    def get_queryset(self):
        return Hardware.objects.filter()
