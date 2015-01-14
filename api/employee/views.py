from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.context_processors import csrf
from forms import EmployeeForm, LanguageForm, EducationForm
from .models import Employee, Language, Education


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
            return HttpResponseRedirect(reverse('employee:languages_list'))
    else:
        f = LanguageForm()

    args = {}
    args.update(csrf(request))
    args['form'] = f

    return render(request, 'language/add.html', {'form': f})


def language_delete(request, language_id):
    language = Language.objects.get(id=language_id)
    language.delete()
    return HttpResponseRedirect(reverse('employee:languages_list'))


def educations_list(request):
    educations = Education.objects.all()

    return render(request, 'education/list.html', {'educations': educations})


def education_edit(request, language_id):
    education = get_object_or_404(Education, pk=language_id)
    return render(request, 'education/edit.html', {'education': education})


def education_add(request):
    if request.method == "POST":
        f = EducationForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect(reverse('employee:educations_list'))
    else:
        f = EducationForm()

    args = {}
    args.update(csrf(request))
    args['form'] = f

    return render(request, 'education/add.html', {'form': f})


def education_delete(request, education_id):
    education = Education.objects.get(id=education_id)
    education.delete()
    return HttpResponseRedirect(reverse('employee:educations_list'))

