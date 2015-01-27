from django.forms import ModelForm, TextInput, Select
from .models import Tag, TagCategory, TagType


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'tag_type', 'tag_category']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'tag_type': Select(attrs={'class': 'form-control'}),
            'tag_category': Select(attrs={'class': 'form-control'}),
        }


class TagCategoryForm(ModelForm):
    class Meta:
        model = TagCategory
        fields = ['name', 'tag_type']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'tag_type': Select(attrs={'class': 'form-control'}),
        }


class TagTypeForm(ModelForm):
    class Meta:
        model = TagType
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        }
