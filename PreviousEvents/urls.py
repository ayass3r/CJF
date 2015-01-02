from django.conf.urls import patterns, url

from PreviousEvents import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
