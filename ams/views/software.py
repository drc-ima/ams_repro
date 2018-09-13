from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import Assets, Software
from ..forms import SoftwareForm
from django.views import generic


class Add(generic.CreateView):
    form_class = SoftwareForm
    success_url = reverse_lazy('ams:assets-software-list')
    template_name = 'ams/assets/software/_software_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class List(LoginRequiredMixin, generic.ListView):
    model = Software
    template_name = 'ams/assets/software/software.html'

    def get_queryset(self):
        return Software.objects.filter(deleted=False)


class ArchiveList(LoginRequiredMixin, generic.ListView):
    model = Software
    template_name = 'ams/assets/software/software-archives.html'

    def get_queryset(self):
        return Software.objects.filter(deleted=True)


class Detail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/software/details-software.html'

    def get_queryset(self):
        return Software.objects.all()


class Update(LoginRequiredMixin, generic.UpdateView):
    form_class = SoftwareForm
    template_name = 'ams/assets/software/update-software.html'
    success_url = reverse_lazy('ams:assets-software-list')

    def get_queryset(self):
        return Software.objects.all()


class Delete(LoginRequiredMixin, generic.DeleteView):
    model = Software
    success_url = reverse_lazy('ams:assets-software-list')
    # template_name = 'ams/assets/details-infrastructure.html'

    def get_queryset(self):
        return Software.objects.filter()