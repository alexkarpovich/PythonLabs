from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import ProjectRole, Project


class ProjectRoleViewList(ListView):
    model = ProjectRole
    context_object_name = 'list'
    paginate_by = 1


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


# Project
class ProjectViewList(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project/project/list.html'


class ProjectViewCreate(CreateView):
    model = Project
    success_url = reverse_lazy('project:project-list')
    template_name = 'project/project/add.html'


class ProjectViewUpdate(UpdateView):
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('project:project-list')
    template_name = 'project/project/edit.html'


class ProjectViewDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project:project-list')
    template_name = 'project/project/delete.html'