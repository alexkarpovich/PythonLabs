from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import ProjectRole, ProjectParticipation


class ProjectRoleViewList(ListView):
    model = ProjectRole
    context_object_name = 'list'
    paginate_by = 10

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by')
        fields = ProjectRole._meta.get_all_field_names()
        if sort_by not in fields:
            sort_by = 'id'
        qs = super(ProjectRoleViewList,self).get_queryset().order_by(sort_by)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ProjectRoleViewList, self).get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort_by')
        return context


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

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by')
        fields = ProjectParticipation._meta.get_all_field_names()
        if sort_by not in fields:
            sort_by = 'id'
        qs = super(ParticipationViewList,self).get_queryset().order_by(sort_by)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ParticipationViewList, self).get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort_by')
        return context


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
