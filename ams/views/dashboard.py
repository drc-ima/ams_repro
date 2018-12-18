from itertools import chain

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic

from ams.models import Department, Staff, Hardware, Software, Information, Infrastructure, SoftwareAssign, \
    HardwareAssign, InformationAssign, InfrastructureAssign, Allocation
from users.models import UserProfile


class Count(LoginRequiredMixin, generic.TemplateView):
    model = Staff
    template_name = 'users/dashboard.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        software = SoftwareAssign.objects.filter(approve=True).count()
        hardware = HardwareAssign.objects.filter(approve=True).count()
        information = InformationAssign.objects.filter(approve=True).count()
        infrastructure = InfrastructureAssign.objects.filter(approve=True).count()
        assets_list = software + hardware + information + infrastructure
        context_data['assets_assigned'] = assets_list
        software = SoftwareAssign.objects.filter(return_it=True).count()
        hardware = HardwareAssign.objects.filter(return_it=True).count()
        information = InformationAssign.objects.filter(return_it=True).count()
        infrastructure = InfrastructureAssign.objects.filter(return_it=True).count()
        assets_list = software + hardware + information + infrastructure
        context_data['assets_returned'] = assets_list
        context_data['staffs'] = Staff.objects.filter(deleted=False).count()
        context_data['staffs_archive'] = Staff.objects.filter(deleted=True).count()
        context_data['departments'] = Department.objects.filter(deleted=False).count()
        context_data['departments_archive'] = Department.objects.filter(deleted=True).count()
        context_data['assets'] = (Hardware.objects.filter(deleted=False).count() + Software.objects.filter(
            deleted=False).count() + Information.objects.filter(deleted=False).count() + Infrastructure.objects.filter(
            deleted=False).count())
        context_data['assets_archive'] = (Hardware.objects.filter(deleted=True).count() + Software.objects.filter(
            deleted=True).count() + Information.objects.filter(deleted=True).count() + Infrastructure.objects.filter(
            deleted=True).count())
        context_data['software'] = Software.objects.filter(deleted=False).count()
        context_data['hardware'] = Hardware.objects.filter(deleted=False).count()
        context_data['information'] = Information.objects.filter(deleted=False).count()
        context_data['infrastructure'] = Infrastructure.objects.filter(deleted=False).count()
        context_data['software_a'] = Software.objects.filter(deleted=True).count()
        context_data['hardware_a'] = Hardware.objects.filter(deleted=True).count()
        context_data['information_a'] = Information.objects.filter(deleted=True).count()
        context_data['infrastructure_a'] = Infrastructure.objects.filter(deleted=True).count()
        context_data['staff_r'] = Staff.objects.filter(deleted=False).latest()
        context_data['departments_r'] = Department.objects.filter(deleted=False).latest()
        context_data['users'] = User.objects.all().count()
        context_data['users_r'] = UserProfile.objects.all().latest()
        software = SoftwareAssign.objects.all()
        hardware = HardwareAssign.objects.all()
        information = InformationAssign.objects.all()
        infrastructure = InfrastructureAssign.objects.all()
        all_a = chain(software, hardware, information, infrastructure)
        context_data['all_a'] = all_a
        context_data['depart_a'] = Allocation.objects.all()
        return context_data


class Bi(LoginRequiredMixin, generic.TemplateView):
    template_name = 'users/dashboard_bi.html'
