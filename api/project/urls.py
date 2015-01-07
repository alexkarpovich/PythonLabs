from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^roles/list/$', views.project_roles_list, name='project-roles-list'),
    url(r'^roles/add/$', views.project_roles_add, name='project-roles-add'),
    url(r'^roles/edit/(?P<id>\d+)/$', views.project_roles_edit, name='project-roles-edit'),
    url(r'^roles/delete/(?P<id>\d+)/$', views.project_roles_delete, name='project-roles-delete'),
)