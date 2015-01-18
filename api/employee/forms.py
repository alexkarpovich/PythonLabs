from models import Employee, Language, Education
from django.forms import ModelForm, TextInput, Select, Textarea


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'summary_description', 'skype', 'phone']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'}),
            'summary_description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Summary'}),
            'skype': TextInput(attrs={'class': 'form-control', 'placeholder': 'Skype'}),
            'phone': TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Phone'}),
        }


class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        }


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        }
