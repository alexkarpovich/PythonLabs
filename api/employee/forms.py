from models import Employee, Language, Education
from django.forms import ModelForm, TextInput, Select, Textarea


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'summary_description', 'skype', 'phone']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'summary_description': Textarea(attrs={'class': 'form-control'}),
            'skype': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control', 'type': 'number'}),
        }


class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }
