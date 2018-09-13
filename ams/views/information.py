from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import Assets, Hardware, Information
from ..forms import HardwareForm, InformationForm
from django.views import generic


class Add(LoginRequiredMixin, generic.CreateView):
    form_class = InformationForm
    success_url = reverse_lazy('ams:assets-information-list')
    template_name = 'ams/assets/information/_information_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class List(LoginRequiredMixin, generic.ListView):
    model = Information
    template_name = 'ams/assets/information/information.html'

    def get_queryset(self):
        return Information.objects.filter(deleted=False)


class ArchiveList(LoginRequiredMixin, generic.ListView):
    model = Information
    template_name = 'ams/assets/information/information-archives.html'

    def get_queryset(self):
        return Information.objects.filter(deleted=True)


class Detail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/information/details-information.html'

    def get_queryset(self):
        return Information.objects.all()


class Update(generic.UpdateView):
    form_class = InformationForm
    template_name = 'ams/assets/information/update-information.html'
    success_url = reverse_lazy('ams:assets-information-list')

    def get_queryset(self):
        return Information.objects.all()


class Delete(generic.DeleteView):
    model = Information
    success_url = reverse_lazy('ams:assets-information-list')
    # template_name = 'ams/assets/details-hardware.html'

    def get_queryset(self):
        return Information.objects.filter()
