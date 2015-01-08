from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.context_processors import csrf
from forms import EmployeeForm, LanguageForm
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
    employee = get_object_or_404(Employee, pk=employee_id)

    return render(request, 'employee/edit.html', {'employee': employee})


def employee_delete(request, employee_id):
    return HttpResponse('Edit delete')


def languages_list(request):
    languages = Language.objects.all()

    return render(request, 'language/list.html', {'languages': languages})


def language_edit(request, language_id):
    language = get_object_or_404(Language, pk=language_id)
    return render(request, 'language/edit.html', {'language': language})


def language_add(request):
    if request.method == "POST":
        f = LanguageForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/employee/languages')
    else:
        f = LanguageForm()

    args = {}
    args.update(csrf(request))
    args['form'] = f

    return render(request, 'language/add.html', {'form': f})


def language_delete(request, language_id):
    return HttpResponse('Delete')
