from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cvbuilder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^employee/', include('employee.urls', namespace='employee')),
    url(r'^spa/', include('spa.urls', namespace='spa')),
)
