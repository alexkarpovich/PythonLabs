from django.contrib import admin
from employee.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'skype', 'phone')
    search_fields = ['first_name', 'last_name', 'email', 'skype', 'phone']

admin.site.register(Employee, EmployeeAdmin)
