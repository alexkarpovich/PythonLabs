from django import forms
import models


class AddProjectRoleForm(forms.ModelForm):
    class Meta():
        model = models.ProjectRole
        fields = ['id','name']
