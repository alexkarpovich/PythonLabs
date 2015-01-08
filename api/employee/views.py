from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.context_processors import csrf
from forms import EmployeeForm

from models import Employee, Language


def employee_list(request):
    employees = Employee.objects.all()

    return render(request, 'employee/list.html', {'employees': employees})


def employee_add(request):
    if request.method == "POST":
        f = EmployeeForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/employee')
    else:
        f = EmployeeForm()

    args = {}
    args.update(csrf(request))
    args['form'] = f

    return render(request, 'employee/add.html', {'form': EmployeeForm()})


def employee_edit(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        raise Http404

    return render(request, 'employee/edit.html', {'employee': employee})

def employee_delete(request):
    return HttpResponse('Edit delete')

def languages_list(request):
    languages = Language.objects.all()

    return render(request, 'language/list.html', {'languages': languages})

def language_edit(request, language_id):
    try:
        language = Language.objects.get(pk=language_id)
    except Language.DoesNotExist:
        raise Http404

    return render(request, 'language/edit.html', {'language': language})

def language_add(request):
    return render(request, 'language/add.html', {})
