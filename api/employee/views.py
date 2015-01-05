from django.http import HttpResponse, Http404
from django.shortcuts import render

from models import Employee

def employee_list(request):
    employees = Employee.objects.all()

    return render(request, 'employee/list.html', {'employees': employees})

def employee_add(request):
    return HttpResponse('Add employee')

def employee_edit(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        raise Http404
    return render(request, 'employee/edit.html', {'employee': employee})

def employee_delete(request):
    return HttpResponse('Edit delete')
