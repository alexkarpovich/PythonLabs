from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import ProjectRole, ProjectPosition
from project.forms import ProjectPositionForm


class ProjectRoleViewList(ListView):
    model = ProjectRole
    context_object_name = 'list'


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


def project_position_list(request):
    return render(request, 'project_position/list.html',
                  {'list': ProjectPosition.objects.all()})


def project_position_add(request):
    if request.method == 'POST':
        form = ProjectPositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project:position-list')

    return render(request, 'project_position/form.html',
                  {'form': ProjectPositionForm()})


def project_position_edit(request, pk):
    position = get_object_or_404(ProjectPosition, pk=pk)
    if request.method == 'POST':
        form = ProjectPositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('project:position-list')

    return render(request, 'project_position/form.html',
                  {'form': ProjectPositionForm(instance=position)})


def project_position_delete(request, pk):
    position = get_object_or_404(ProjectPosition, pk=pk)
    position.delete()
    return redirect('project:position-list')