from django import forms
import models


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