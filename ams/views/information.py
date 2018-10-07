from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import Information
from ..forms import InformationForm, InformationAssignForm
from django.views import generic


class Add(LoginRequiredMixin, generic.CreateView):
    form_class = InformationForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/information/_information_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


"""
class List(LoginRequiredMixin, generic.ListView):
    model = Information
    template_name = 'ams/assets/information/information.html'

    def get_queryset(self):
        return Information.objects.filter(deleted=False)



class ArchiveList(LoginRequiredMixin, generic.ListView):
    model = Assets
    template_name = 'ams/assets/information/information-archives.html'

    def get_queryset(self):
        return Assets.objects.filter(deleted=True)
"""


class Detail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/information/details-information.html'

    def get_queryset(self):
        return Information.objects.all()


class Update(generic.UpdateView):
    form_class = InformationForm
    template_name = 'ams/assets/information/update-information.html'
    success_url = reverse_lazy('ams:assets-list')

    def get_queryset(self):
        return Information.objects.all()


class Archive(generic.DeleteView):
    model = Information
    success_url = reverse_lazy('ams:assets-list')
    # template_name = 'ams/assets/details-hardware.html'

    def get_queryset(self):
        return Information.objects.delete()


class Assign(LoginRequiredMixin, generic.CreateView):
    form_class = InformationAssignForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/assign/_hardware_assign.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Restore(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:assets-list')
    model = Information

    def get_queryset(self):
        return Information.objects.undelete()

