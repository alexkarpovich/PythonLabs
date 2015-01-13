from django.conf.urls import patterns, url

import views
from .views import ProjectRoleViewList, ProjectRoleViewCreate, ProjectRoleViewUpdate, ProjectRoleViewDelete, ProjectViewList
urlpatterns = patterns('',
    url(r'^$', ProjectViewList.as_view(), name='project-list'),
    url(r'^role/list/$', ProjectRoleViewList.as_view(), name='role-list'),
    url(r'^role/add/$', ProjectRoleViewCreate.as_view(), name='role-add'),
    url(r'^role/edit/(?P<pk>\d+)/$', ProjectRoleViewUpdate.as_view(), name='role-edit'),
    url(r'^role/delete/(?P<pk>\d+)/$', ProjectRoleViewDelete.as_view(), name='role-delete'),
)
