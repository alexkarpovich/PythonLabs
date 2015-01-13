from django.conf.urls import patterns, url
import views
from .views import ProjectRoleViewList, ProjectRoleViewCreate, ProjectRoleViewUpdate, ProjectRoleViewDelete

urlpatterns = patterns('',
    url(r'^$', views.ProjectViewList.as_view(), name='project-list'),
    url(r'^add/$', views.ProjectViewCreate.as_view(), name='project-add'),
    url(r'^edit(?P<pk>\d+)/$', views.ProjectViewUpdate.as_view(), name='project-edit'),
    url(r'^delete/(?P<pk>\d+)$', views.ProjectViewDelete.as_view(), name='project-delete'),

    url(r'^role/list/$', ProjectRoleViewList.as_view(), name='role-list'),
    url(r'^role/add/$', ProjectRoleViewCreate.as_view(), name='role-add'),
    url(r'^role/edit/(?P<pk>\d+)/$', ProjectRoleViewUpdate.as_view(), name='role-edit'),
    url(r'^role/delete/(?P<pk>\d+)/$', ProjectRoleViewDelete.as_view(), name='role-delete'),
)
