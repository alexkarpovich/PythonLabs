from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from models import ProjectRole
from forms import AddProjectRoleForm


def project_roles_list(request):
    project_roles_list = ProjectRole.objects.all()
    context = {
        'project_roles':project_roles_list
    }
    return render(request, 'project/project_roles_list.html',context)

def project_roles_add(request):
    if request.method == 'POST':
        addProjectRoleForm = AddProjectRoleForm(request.POST)
        addProjectRoleForm.save()

        return redirect('/project/roles/list/')
    elif request.method == 'GET':
        context = {}
        context.update(csrf(request))
        return render(request, 'project/project_roles_add.html', context)

def project_roles_edit(request, id):
    if request.method == 'POST':
        instance = ProjectRole.objects.get(pk=id)
        editProjectRoleForm = AddProjectRoleForm(request.POST, instance=instance)
        editProjectRoleForm.save()

        return redirect('/project/roles/list')
        return ''
    elif request.method == 'GET':
        role = ProjectRole.objects.get(pk=id)
        context = {
            'role': role
        }
        context.update(csrf(request))
        return render(request, 'project/project_roles_edit.html', context)
    return ""

def project_roles_delete(request, id):
    if request.method == 'GET':
        role = ProjectRole.objects.get(pk=id)
        if role:
            role.delete()
    return redirect('/project/roles/list/')