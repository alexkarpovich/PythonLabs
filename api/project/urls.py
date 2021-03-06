from django.conf.urls import patterns, url

from views import *
urlpatterns = patterns('',
    url(r'^$', ProjectViewList.as_view(), name='project-list'),
    url(r'^add/$', ProjectViewCreate.as_view(), name='project-add'),
    url(r'^edit/(?P<pk>\d+)/$', ProjectViewUpdate.as_view(), name='project-edit'),
    url(r'^delete/(?P<pk>\d+)$', ProjectViewDelete.as_view(), name='project-delete'),

    url(r'^status/$', ProjectStatusViewList.as_view(), name='status-list'),
    url(r'^status/add/$', ProjectStatusViewCreate.as_view(), name='status-add'),
    url(r'^status/edit/(?P<pk>\d+)/$', ProjectStatusViewUpdate.as_view(), name='status-edit'),
    url(r'^status/delete/(?P<pk>\d+)$', ProjectStatusViewDelete.as_view(), name='status-delete'),

    url(r'^role/list/$', ProjectRoleViewList.as_view(), name='role-list'),
    url(r'^role/add/$', ProjectRoleViewCreate.as_view(), name='role-add'),
    url(r'^role/edit/(?P<pk>\d+)/$', ProjectRoleViewUpdate.as_view(), name='role-edit'),
    url(r'^role/delete/(?P<pk>\d+)/$', ProjectRoleViewDelete.as_view(), name='role-delete'),

    url(r'^participation/list/$', ParticipationViewList.as_view(), name='participation-list'),
    url(r'^participation/add/$', ParticipationViewCreate.as_view(), name='participation-add'),
    url(r'^participation/edit/(?P<pk>\d+)/$', ParticipationViewUpdate.as_view(), name='participation-edit'),
    url(r'^participation/delete/(?P<pk>\d+)/$', ParticipationViewDelete.as_view(), name='participation-delete'),

    url(r'^position/list/$', PositionViewList.as_view(), name='position-list'),
    url(r'^position/add/$', PositionViewCreate.as_view(), name='position-add'),
    url(r'^position/edit/(?P<pk>\d+)/$', PositionViewUpdate.as_view(), name='position-edit'),
    url(r'^position/delete/(?P<pk>\d+)/$', PositionViewDelete.as_view(), name='position-delete'),

    url(r'^tag/list/$', ProjectTagViewList.as_view(), name='tag-list'),
    url(r'^tag/add/$', ProjectTagViewCreate.as_view(), name='tag-add'),
    url(r'^tag/edit/(?P<pk>\d+)/$', ProjectTagViewUpdate.as_view(), name='tag-edit'),
    url(r'^tag/delete/(?P<pk>\d+)/$', ProjectTagViewDelete.as_view(), name='tag-delete'),
)
