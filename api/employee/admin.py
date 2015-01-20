from django.contrib import admin
from .models import Employee, Language, EmployeeLanguage, Education, EmployeeEducation, EmployeeTag


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'skype', 'phone')
    search_fields = ['first_name', 'last_name', 'email', 'skype', 'phone']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Language)
admin.site.register(EmployeeLanguage)
admin.site.register(Education)
admin.site.register(EmployeeEducation)
admin.site.register(EmployeeTag)

