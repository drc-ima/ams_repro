from django.urls import reverse_lazy
from ..models import Assets, Infrastructure
from ..forms import InfrastructureForm
from django.views import generic


class Add(generic.CreateView):
    form_class = InfrastructureForm
    success_url = reverse_lazy('ams:assets-infrastructure-list')
    template_name = 'ams/assets/Infrastructure/_infrastructure_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class List(generic.ListView):
    model = Infrastructure
    template_name = 'ams/assets/infrastructure/infrastructure.html'

    def get_queryset(self):
        return Infrastructure.objects.filter(deleted=False)


class ArchiveList(generic.ListView):
    model = Infrastructure
    template_name = 'ams/assets/Infrastructure/Infrastructure-archives.html'

    def get_queryset(self):
        return Infrastructure.objects.filter(deleted=True)


class Detail(generic.DetailView):
    # model = infrastructure
    # select_related = ('infrastructure_staff',)
    template_name = 'ams/assets/Infrastructure/details-Infrastructure.html'

    def get_queryset(self):
        return Infrastructure.objects.all()


class Update(generic.UpdateView):
    form_class = InfrastructureForm
    template_name = 'ams/assets/infrastructure/update-infrastructure.html'
    success_url = reverse_lazy('ams:assets-infrastructure-list')

    def get_queryset(self):
        return Infrastructure.objects.all()


class Delete(generic.DeleteView):
    model = Infrastructure
    success_url = reverse_lazy('ams:assets-infrastructure-list')
    # template_name = 'ams/assets/details-infrastructure.html'

    def get_queryset(self):
        return Infrastructure.objects.filter()
