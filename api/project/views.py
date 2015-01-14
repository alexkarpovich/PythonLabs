from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import ProjectRole, ProjectParticipation


class ProjectRoleViewList(ListView):
    model = ProjectRole
    context_object_name = 'list'
    paginate_by = 10


class ProjectRoleViewCreate(CreateView):
    model = ProjectRole
    success_url = reverse_lazy('project:role-list')


class ProjectRoleViewUpdate(UpdateView):
    model = ProjectRole
    success_url = reverse_lazy('project:role-list')
    template_name_suffix = '_edit'
    context_object_name = 'role'


class ProjectRoleViewDelete(DeleteView):
    model = ProjectRole
    success_url = reverse_lazy('project:role-list')


class ParticipationViewList(ListView):
    model = ProjectParticipation
    context_object_name = 'list'
    paginate_by = 10


class ParticipationViewCreate(CreateView):
    model = ProjectParticipation
    success_url = reverse_lazy('project:participation-list')


class ParticipationViewUpdate(UpdateView):
    model = ProjectParticipation
    success_url = reverse_lazy('project:participation-list')
    template_name_suffix = '_edit'
    context_object_name = 'participation'


class ParticipationViewDelete(DeleteView):
    model = ProjectParticipation
    success_url = reverse_lazy('project:participation-list')
