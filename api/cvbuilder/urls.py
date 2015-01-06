from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^employee/', include('employee.urls', namespace='employee')),
    url(r'^spa/', include('spa.urls', namespace='spa')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
