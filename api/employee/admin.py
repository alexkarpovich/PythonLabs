from django.contrib import admin
from models import Employee, Language, EmployeeLanguage
from tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline


class TagInline(GenericTabularInline):
    model = TaggedItem
    extra = 0


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'skype', 'phone')
    search_fields = ['first_name', 'last_name', 'email', 'skype', 'phone']
    inlines = (TagInline,)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Language)
admin.site.register(EmployeeLanguage)

