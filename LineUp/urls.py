from django.conf.urls import patterns, url

from LineUp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
