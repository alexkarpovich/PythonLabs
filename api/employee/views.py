from forms import EmployeeForm, LanguageForm, EducationForm
from .models import Employee, Language, Education
from django.views.generic.edit import UpdateView, DeleteView, FormView
from api.base.views import BaseListView
from django.core.urlresolvers import reverse_lazy


class EmployeeViewList(BaseListView):
    model = Employee
    fields = ['first_name', 'last_name', 'skype', 'phone']
    context_object_name = 'list'


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
