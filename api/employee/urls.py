from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.employee_list, name='employee_list'),
    url(r'^add/$', views.employee_add, name='employee_add'),
    url(r'^edit/(?P<employee_id>\d+)/$', views.employee_edit, name='employee_edit'),
    url(r'^delete/(?P<employee_id>\d+)$', views.employee_delete, name='employee_delete'),
    url(r'^languages/$', views.languages_list, name='languages_list'),
    url(r'^language/edit/(?P<language_id>\d+)$', views.language_edit, name='language_edit'),
    url(r'^language/add/$', views.language_add, name='language_add'),
    url(r'^language/delete/(?P<language_id>\d+)$', views.language_delete, name='language_delete'),
    url(r'^educations/$', views.educations_list, name='educations_list'),
    url(r'^education/edit/(?P<education_id>\d+)$', views.education_edit, name='education_edit'),
    url(r'^education/add/$', views.education_add, name='education_add'),
    url(r'^education/delete/(?P<education_id>\d+)$', views.education_delete, name='education_delete'),
)
