from django.conf.urls import patterns, url
from SpecialGuests import views

urlpatterns = patterns('',
    url(r'^$', views.specialguests, name='specialguests'),
)
