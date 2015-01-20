from models import Employee, Language, Education, EmployeeTag
from django.forms import ModelForm, TextInput, Textarea, Select, FileInput


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'summary_description', 'skype', 'phone', 'photo']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'}),
            'summary_description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Summary'}),
            'skype': TextInput(attrs={'class': 'form-control', 'placeholder': 'Skype'}),
            'phone': TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Phone'}),
            'photo': FileInput(attrs={'class': 'form-control', 'type': 'file', 'placeholder': 'Photo'}),
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


class EmployeeTagForm(ModelForm):
    class Meta:
        model = EmployeeTag
        fields = ['employee', 'tag', 'level', 'experience', 'last_used']
        widgets = {
            'employee': Select(attrs={'class': 'form-control'}),
            'tag': Select(attrs={'class': 'form-control'}),
            'level': Select(attrs={'class': 'form-control'}),
            'experience': TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience(years)', 'type': 'number'}),
            'last_used': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Used', 'type': 'date'}),
        }