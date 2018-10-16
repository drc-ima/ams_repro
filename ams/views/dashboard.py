from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from ams.models import Department, Staff, Hardware, Software, Information, Infrastructure


class Count(LoginRequiredMixin, generic.TemplateView):
    model = Staff
    template_name = 'users/dashboard.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
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
        return context_data
