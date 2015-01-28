from forms import EmployeeForm, LanguageForm, EducationForm, EmployeeTagForm
from .models import Employee, Language, Education, EmployeeTag
from django.views.generic.edit import UpdateView, DeleteView, FormView
from api.base.views import BaseListView
from django.core.urlresolvers import reverse_lazy


class EmployeeViewList(BaseListView):
    model = Employee
    fields = ['first_name', 'last_name', 'skype', 'phone', 'photo']
    context_object_name = 'list'
    sort_fields = ['id', 'first_name', 'last_name', 'skype', 'phone']


class EmployeeViewAdd(FormView):
    template_name = 'employee/employee_add_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee:employee_list')

    def form_valid(self, form):
        form.save()
        return super(EmployeeViewAdd, self).form_valid(form)


class EmployeeViewUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_edit_form.html'
    success_url = reverse_lazy('employee:employee_list')


class EmployeeViewDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee:employee_list')


class LanguageViewList(BaseListView):
    model = Language
    fields = ['name']
    context_object_name = 'list'
    sort_fields = ['name']


class LanguageViewAdd(FormView):
    template_name = 'employee/language_add_form.html'
    form_class = LanguageForm
    success_url = reverse_lazy('employee:languages_list')

    def form_valid(self, form):
        form.save()
        return super(LanguageViewAdd, self).form_valid(form)


class LanguageViewUpdate(UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = 'employee/language_edit_form.html'
    success_url = reverse_lazy('employee:languages_list')


class LanguageViewDelete(DeleteView):
    model = Language
    success_url = reverse_lazy('employee:languages_list')


class EducationViewList(BaseListView):
    model = Education
    fields = ['name']
    context_object_name = 'list'
    sort_fields = ['id', 'name']


class EducationViewAdd(FormView):
    template_name = 'employee/education_add_form.html'
    form_class = EducationForm
    success_url = reverse_lazy('employee:educations_list')

    def form_valid(self, form):
        form.save()
        return super(EducationViewAdd, self).form_valid(form)


class EducationViewUpdate(UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'employee/education_edit_form.html'
    success_url = reverse_lazy('employee:educations_list')


class EducationViewDelete(DeleteView):
    model = Education
    success_url = reverse_lazy('employee:educations_list')


class EmployeeTagViewList(BaseListView):
    model = EmployeeTag
    fields = ['name']
    context_object_name = 'list'
    sort_fields = ['id', 'name']


class EmployeeTagViewAdd(FormView):
    template_name = 'employee/employeetag_add_form.html'
    form_class = EmployeeTagForm
    success_url = reverse_lazy('employee:employee_tags_list')

    def form_valid(self, form):
        form.save()
        return super(EmployeeTagViewAdd, self).form_valid(form)


class EmployeeTagViewUpdate(UpdateView):
    model = EmployeeTag
    form_class = EmployeeTagForm
    template_name = 'employee/employeetag_edit_form.html'
    success_url = reverse_lazy('employee:employee_tags_list')


class EmployeeTagViewDelete(DeleteView):
    model = EmployeeTag
    success_url = reverse_lazy('employee:employee_tags_list')