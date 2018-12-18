# from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# from django.utils import timezone
from django.views import generic

from ams import models
from ams.forms import DepartmentForm, DepartmentLeadForm, AllocateDepartmentForm
from ams.models import Department


class Add(LoginRequiredMixin, generic.CreateView):
    form_class = DepartmentForm
    success_url = reverse_lazy('ams:department-list')
    template_name = 'ams/department/_department_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Allocate(LoginRequiredMixin, generic.CreateView):
    form_class = AllocateDepartmentForm
    template_name = 'ams/department/_allocate_form.html'
    success_url = reverse_lazy('ams:department-list')

    def form_valid(self, form):
        form.instance.allocated_by = self.request.user
        return super(Allocate, self).form_valid(form)


class AddLead(LoginRequiredMixin, generic.CreateView):
    form_class = DepartmentLeadForm
    template_name = 'ams/department/_lead_form.html'
    success_url = reverse_lazy('ams:department-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class List(LoginRequiredMixin, generic.ListView):
    model = Department
    template_name = 'ams/department/department.html'
    paginate_by = 10
    queryset = Department.objects.filter(deleted=False)
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['department_archives'] = Department.objects.filter(deleted=True)
        context_data['member'] = models.Allocation.objects.all()
        return context_data
    """    
    def get_queryset(self):
        return Department.objects.filter()
    """


class ArchiveList(LoginRequiredMixin, generic.ListView):
    model = Department
    template_name = 'ams/department/department-archives.html'
    paginate_by = 10
    queryset = Department.objects.filter(deleted=True)
    context_object_name = 'department_archives'

    def get_queryset(self):
        return Department.objects.filter(deleted=True)


class ArchiveDetail(LoginRequiredMixin, generic.DetailView):
    # model = Hardware
    # select_related = ('hardware_staff',)
    template_name = 'ams/department/department-archive-detail.html'

    def get_queryset(self):
        return Department.objects.all()


class Detail(LoginRequiredMixin, generic.DetailView):
    model = models.Allocation
    template_name = 'ams/department/details-department.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = models.Allocation.objects.all()
        return context

    def get_queryset(self):
        return Department.objects.all()


class Update(LoginRequiredMixin, generic.UpdateView):
    form_class = DepartmentForm
    template_name = 'ams/department/update-department.html'
    success_url = reverse_lazy('ams:department-list')

    def get_queryset(self):
        return Department.objects.all()


class Delete(LoginRequiredMixin, generic.DeleteView):
    model = Department
    success_url = reverse_lazy('ams:department-list')
    # template_name = 'ams/assets/details-hardware.html'

    def get_queryset(self):
        return Department.objects.filter()


class Restore(LoginRequiredMixin, generic.UpdateView):
    success_url = reverse_lazy('ams:department-list')
    model = Department
    fields = ['deleted', ]

    def get_queryset(self):
        return Department.objects.filter()


class HardDelete(LoginRequiredMixin, generic.DeleteView):
    model = Department
    success_url = reverse_lazy('ams:department-archive-list')

    def get_queryset(self):
        return Department.objects.filter()
