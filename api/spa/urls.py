from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.spa_home, name='spa_home'),
)