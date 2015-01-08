from django.forms import ModelForm
from models import Employee, Language


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'summary_description', 'skype', 'phone']


class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ['name']
