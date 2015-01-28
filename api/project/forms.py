from django import forms
import models
from django.forms import ModelForm, TextInput, Textarea, Select


class AddProjectRoleForm(forms.ModelForm):
    class Meta():
        model = models.ProjectRole
        fields = ['id', 'name']


class AddProjectParticipationForm(forms.ModelForm):
    class Meta():
        model = models.ProjectParticipation
        fields = ['id', 'name']


class ProjectPositionForm(forms.ModelForm):
    class Meta():
        model = models.ProjectPosition
        fields = ['id', 'name']


class ProjectTagForm(forms.ModelForm):
    class Meta():
        model = models.ProjectTag
        fields = ['project', 'tag',]

        widgets = {
            'project': Select(attrs={'class': 'form-control'}),
            'tag': Select(attrs={'class': 'form-control'}),
        }