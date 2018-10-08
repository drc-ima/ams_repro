from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import Infrastructure
from ..forms import InfrastructureForm, InfrastructureAssignForm
from django.views import generic


class Add(LoginRequiredMixin, generic.CreateView):
    form_class = InfrastructureForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/Infrastructure/_infrastructure_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


"""
class List(generic.ListView):
    model = Infrastructure
    template_name = 'ams/assets/infrastructure/infrastructure.html'

    def get_queryset(self):
        return Infrastructure.objects.filter(deleted=False)
"""


class ArchiveList(generic.ListView):
    model = Infrastructure
    template_name = 'ams/assets/Infrastructure/Infrastructure-archives.html'

    def get_queryset(self):
        return Infrastructure.objects.filter(deleted=True)


class ArchiveDetail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/infrastructure/infrastructure-archive-detail.html'

    def get_queryset(self):
        return Infrastructure.objects.all()


class Detail(LoginRequiredMixin, generic.DetailView):
    # model = infrastructure
    # select_related = ('infrastructure_staff',)
    template_name = 'ams/assets/Infrastructure/details-Infrastructure.html'

    def get_queryset(self):
        return Infrastructure.objects.all()


class Update(LoginRequiredMixin, generic.UpdateView):
    form_class = InfrastructureForm
    template_name = 'ams/assets/infrastructure/update-infrastructure.html'
    success_url = reverse_lazy('ams:assets-list')

    def get_queryset(self):
        return Infrastructure.objects.all()


class Archive(LoginRequiredMixin, generic.DeleteView):
    model = Infrastructure
    success_url = reverse_lazy('ams:assets-list')
    # template_name = 'ams/assets/details-infrastructure.html'

    def get_queryset(self):
        return Infrastructure.objects.filter()


class Restore(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:assets-list')
    model = Infrastructure
    fields = ['deleted', ]

    def get_queryset(self):
        return Infrastructure.objects.filter()


class Assign(LoginRequiredMixin, generic.CreateView):
    form_class = InfrastructureAssignForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/assign/_hardware_assign.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
