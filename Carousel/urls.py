from django.conf.urls import patterns, url
from Carousel import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
)