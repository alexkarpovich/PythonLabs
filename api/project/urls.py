from django.conf.urls import patterns, url

from views import *
urlpatterns = patterns('',
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
)
