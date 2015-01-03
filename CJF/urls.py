from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CJF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^artists/', include('LineUp.urls')),
    url(r'^previous/', include('PreviousEvents.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
