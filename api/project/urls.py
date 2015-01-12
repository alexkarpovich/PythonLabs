from django.conf.urls import patterns, url

import views
from .views import ProjectRoleViewList, ProjectRoleViewCreate, ProjectRoleViewUpdate, ProjectRoleViewDelete
urlpatterns = patterns('',
    url(r'^role/list/$', views.project_roles_list, name='role-list'),
    url(r'^role/add/$', views.project_roles_add, name='role-add'),
    url(r'^role/edit/(?P<id>\d+)/$', views.project_roles_edit, name='role-edit'),
    url(r'^role/delete/(?P<id>\d+)/$', views.project_roles_delete, name='role-delete'),

    url(r'^position/list/$', views.project_roles_list, name='position-list'),
    url(r'^position/add/$', views.project_roles_add, name='position-add'),
    url(r'^position/edit/(?P<id>\d+)/$', views.project_roles_edit, name='position-edit'),
    url(r'^position/delete/(?P<id>\d+)/$', views.project_roles_delete, name='position-delete'),
)
