from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import ProjectRole, ProjectParticipation
from api.index.views import ExtendedListView


class ProjectRoleViewList(ExtendedListView):
    model = ProjectRole


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


class ParticipationViewList(ExtendedListView):
    model = ProjectParticipation


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
