from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import Assets
from ..forms import HardwareForm, AssignForm
from django.views import generic


class List(LoginRequiredMixin, generic.ListView):
    template_name = 'ams/assets/assets.html'
    model = Assets

    def get_queryset(self):
        return Assets.objects.all()


class Assign(LoginRequiredMixin, generic.CreateView):
    template_name = 'ams/assets/asset_temp.html'
    form_class = AssignForm
    success_url = reverse_lazy('ams:assets-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
