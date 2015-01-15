from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.context_processors import csrf
from forms import EmployeeForm, LanguageForm, EducationForm
from .models import Employee, Language, Education
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


ITEMS_PER_PAGE = 7


def employee_list(request):
    employees = Employee.objects.all()
    paginator = Paginator(employees, ITEMS_PER_PAGE)
    page = request.GET.get('page')

    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)

    return render(request, 'employee/list.html', {'employees': employees})


def employee_add(request):
    if request.method == "POST":
        f = EmployeeForm(request.POST or None)
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
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == "POST":
        employee.delete()
        return HttpResponseRedirect(reverse('employee:employee_list'))
    else:
        return render(request, 'employee/confirm_delete.html', {'employee': employee})


def languages_list(request):
    languages = Language.objects.all()
    paginator = Paginator(languages, ITEMS_PER_PAGE)
    page = request.GET.get('page')

    try:
        languages = paginator.page(page)
    except PageNotAnInteger:
        languages = paginator.page(1)
    except EmptyPage:
        languages = paginator.page(paginator.num_pages)

    return render(request, 'language/list.html', {'languages': languages})


def language_edit(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    f = LanguageForm(request.POST or None, instance=language)
    if f.is_valid():
        f.save()
        return HttpResponseRedirect(reverse('employee:languages_list'))
    return render(request, 'language/edit.html', {'form': f, 'id': language.id})


def language_add(request):
    if request.method == "POST":
        f = LanguageForm(request.POST or None)
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
    language = get_object_or_404(Language, pk=language_id)
    if request.method == "POST":
        language.delete()
        return HttpResponseRedirect(reverse('employee:languages_list'))
    else:
        return render(request, 'language/confirm_delete.html', {'language': language})


def educations_list(request):
    educations = Education.objects.all()
    paginator = Paginator(educations, ITEMS_PER_PAGE)
    page = request.GET.get('page')

    try:
        educations = paginator.page(page)
    except PageNotAnInteger:
        educations = paginator.page(1)
    except EmptyPage:
        educations = paginator.page(paginator.num_pages)

    return render(request, 'education/list.html', {'educations': educations})


def education_edit(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    f = EducationForm(request.POST or None, instance=education)
    if f.is_valid():
        f.save()
        return HttpResponseRedirect(reverse('employee:educations_list'))
    return render(request, 'education/edit.html', {'form': f, 'id': education.id})


def education_add(request):
    if request.method == "POST":
        f = EducationForm(request.POST or None)
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
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        return HttpResponseRedirect(reverse('employee:educations_list'))
    else:
        return render(request, 'education/confirm_delete.html', {'education': education})

