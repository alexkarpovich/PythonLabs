from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.employee_list, name='employee_list'),
    url(r'^add/$', views.employee_add, name='employee_add'),
    url(r'^edit/(?P<employee_id>\d+)/$', views.employee_edit, name='employee_edit'),
    url(r'^delete/(?P<employee_id>\d+)$', views.employee_delete, name='employee_delete'),
)
