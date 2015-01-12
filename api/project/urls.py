from django.conf.urls import patterns, url
from project.models import ProjectRole

import views
from .views import ProjectRoleViewList, ProjectRoleViewCreate, ProjectRoleViewUpdate, ProjectRoleViewDelete
urlpatterns = patterns('',
    url(r'^role/list/$', ProjectRoleViewList.as_view(), name='role-list'),
    url(r'^role/add/$', ProjectRoleViewCreate.as_view(), name='role-add'),
    url(r'^role/edit/(?P<pk>\d+)/$', ProjectRoleViewUpdate.as_view(), name='role-edit'),
    url(r'^role/delete/(?P<pk>\d+)/$', ProjectRoleViewDelete.as_view(), name='role-delete'),

    url(r'^position/list/$', views.project_position_list, name='position-list'),
    url(r'^position/add/$', views.project_position_add, name='position-add'),
    url(r'^position/edit/(?P<pk>\d+)/$', views.project_position_edit, name='position-edit'),
    url(r'^position/delete/(?P<pk>\d+)/$', views.project_position_delete, name='position-delete'),
)
