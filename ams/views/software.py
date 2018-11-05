from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ams import models, forms
from ams.models import Software
from ..forms import SoftwareForm
from django.views import generic


class Add(generic.CreateView):
    form_class = SoftwareForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/software/_software_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ArchiveDetail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/software/software-archive-detail.html'

    def get_queryset(self):
        return Software.objects.all()


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
        return models.Software.objects.all()


class Update(LoginRequiredMixin, generic.UpdateView):
    form_class = SoftwareForm
    template_name = 'ams/assets/software/update-software.html'
    success_url = reverse_lazy('ams:assets-list')

    def get_queryset(self):
        return models.Software.objects.all()


class Archive(LoginRequiredMixin, generic.DeleteView):
    model = models.Software
    success_url = reverse_lazy('ams:assets-list')

    def get_queryset(self):
        return models.Software.objects.filter()


class Assign(LoginRequiredMixin, generic.CreateView):
    form_class = forms.SoftwareAssignForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/assign/_software_assign.html'

    def form_valid(self, form):
        form.instance.assign_by = self.request.user
        return super(Assign, self).form_valid(form)


class Owner(LoginRequiredMixin, generic.CreateView):
    form_class = forms.SoftwareOwnerForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/owner/_software_owner.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Restore(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:assets-list')
    model = models.Software
    fields = ['deleted', ]

    def get_queryset(self):
        return models.Software.objects.filter()


class ApproveDetail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/software/approve-details-software.html'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return models.SoftwareAssign.objects.all()


class Approve(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:assign-list')
    form_class = forms.SoftwareApproveForm
    # fields = ['approve', ]
    template_name = 'ams/assets/software/approve-details-software.html'

    def get_queryset(self):
        return models.SoftwareAssign.objects.filter()
