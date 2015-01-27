from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

from models import ProjectRole, ProjectParticipation, ProjectPosition, ProjectTag
from .forms import ProjectTagForm
from base.views import BaseListView


class ProjectRoleViewList(BaseListView):
    model = ProjectRole
    sort_fields = ['id','name']


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


class ParticipationViewList(BaseListView):
    model = ProjectParticipation
    sort_fields = ['id', 'name']


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


# Project position
class PositionViewList(BaseListView):
    model = ProjectPosition
    template_name = 'project_position/list.html'


class PositionViewCreate(CreateView):
    model = ProjectPosition
    success_url = reverse_lazy('project:position-list')
    template_name = 'project_position/add.html'


class PositionViewUpdate(UpdateView):
    model = ProjectPosition
    success_url = reverse_lazy('project:position-list')
    context_object_name = 'position'
    template_name = 'project_position/edit.html'


class PositionViewDelete(DeleteView):
    model = ProjectPosition
    success_url = reverse_lazy('project:position-list')
    template_name = 'project_position/confirm_delete.html'


# Project tag
class ProjectTagViewList(BaseListView):
    model = ProjectTag
    sort_fields = ['tag', 'project']


class ProjectTagViewCreate(FormView):
    model = ProjectTag
    form_class = ProjectTagForm
    success_url = reverse_lazy('project:tag-list')
    template_name = 'project/projecttag_add_form.html'

    def form_valid(self, form):
        form.save()
        return super(ProjectTagViewCreate, self).form_valid(form)


class ProjectTagViewUpdate(UpdateView):
    model = ProjectTag
    form_class = ProjectTagForm
    success_url = reverse_lazy('project:tag-list')
    template_name = 'project/projecttag_edit_form.html'


class ProjectTagViewDelete(DeleteView):
    model = ProjectTag
    success_url = reverse_lazy('project:tag-list')
    template_name = 'project/projecttag_confirm_delete.html'

