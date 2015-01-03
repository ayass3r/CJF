from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CJF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^artists/', include('LineUp.urls')),
    url(r'^presvoiusfestivals/', include('PreviousEvents.urls')),
    
)
