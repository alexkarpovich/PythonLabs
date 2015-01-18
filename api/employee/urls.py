from django.conf.urls import patterns, url

import views
from .views import EmployeeViewList, EmployeeViewUpdate, EmployeeViewAdd, EmployeeViewDelete, \
    LanguageViewList, LanguageViewAdd, LanguageViewUpdate, LanguageViewDelete, \
    EducationViewList, EducationViewAdd, EducationViewUpdate, EducationViewDelete

urlpatterns = patterns('',
    url(r'^$', EmployeeViewList.as_view(), name='employee_list'),
    url(r'^add/$', EmployeeViewAdd.as_view(), name='employee_add'),
    url(r'^edit/(?P<pk>\d+)/$', EmployeeViewUpdate.as_view(), name='employee_edit'),
    url(r'^delete/(?P<pk>\d+)$', EmployeeViewDelete.as_view(), name='employee_delete'),
    url(r'^languages/$', LanguageViewList.as_view(), name='languages_list'),
    url(r'^language/add/$', LanguageViewAdd.as_view(), name='language_add'),
    url(r'^language/edit/(?P<pk>\d+)$', LanguageViewUpdate.as_view(), name='language_edit'),
    url(r'^language/delete/(?P<pk>\d+)$', LanguageViewDelete.as_view(), name='language_delete'),
    url(r'^educations/$', EducationViewList.as_view(), name='educations_list'),
    url(r'^education/add/$', EducationViewAdd.as_view(), name='education_add'),
    url(r'^education/edit/(?P<pk>\d+)$', EducationViewUpdate.as_view(), name='education_edit'),
    url(r'^education/delete/(?P<pk>\d+)$', EducationViewDelete.as_view(), name='education_delete'),
)
