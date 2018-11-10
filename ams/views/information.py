from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from ams import models, forms
from ..models import Information
from ..forms import InformationForm, InformationAssignForm, InformationOwnerForm
from django.views import generic


class Add(LoginRequiredMixin, generic.CreateView):
    form_class = InformationForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/information/_information_form.html'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(Add, self).form_valid(form)


"""
class List(LoginRequiredMixin, generic.ListView):
    model = Information
    template_name = 'ams/assets/information/information.html'

    def get_queryset(self):
        return Information.objects.filter(deleted=False)
"""


class ArchiveList(LoginRequiredMixin, generic.ListView):
    model = Information
    template_name = 'ams/assets/information/information-archives.html'

    def get_queryset(self):
        return Information.objects.filter(deleted=True)


class ArchiveDetail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/information/information-archive-detail.html'

    def get_queryset(self):
        return Information.objects.all()


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
        return Information.objects.filter()


class Assign(LoginRequiredMixin, generic.CreateView):
    form_class = InformationAssignForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/assign/_information_assign.html'

    def form_valid(self, form):
        form.instance.assign_by = self.request.user
        return super(Assign, self).form_valid(form)


class Owner(LoginRequiredMixin, generic.CreateView):
    form_class = InformationOwnerForm
    success_url = reverse_lazy('ams:assets-list')
    template_name = 'ams/assets/owner/_information_owner.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Restore(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:assets-list')
    model = Information
    fields = ['deleted', ]

    def get_queryset(self):
        return Information.objects.filter()


class Delete(LoginRequiredMixin, generic.DeleteView):
    model = Information
    success_url = reverse_lazy('ams:assets-information-archive-list')

    def get_queryset(self):
        return Information.objects.filter().delete()


class ApproveDetail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/assets/information/approve-details-information.html'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return models.InformationAssign.objects.all()


class Approve(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:assign-list')
    form_class = forms.InformationApproveForm
    # fields = ['approve', ]
    template_name = 'ams/assets/information/approve-details-information.html'

    def get_queryset(self):
        return models.InformationAssign.objects.filter()

