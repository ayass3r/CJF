from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
  
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artists/', include('LineUp.urls')),
    url(r'^previous/', include('PreviousEvents.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
