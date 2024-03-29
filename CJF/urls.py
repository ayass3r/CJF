from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
  
    url(r'^admin/', include(admin.site.urls)),
    url(r'^program/', include('LineUp.urls')),
    url(r'^home/', include('Carousel.urls')),
    url(r'^specialguests/', include('SpecialGuests.urls')),


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^aboutus/$', 'flatpage', {'url': '/aboutus/'}, name='Cairo Jazz Festival - About Us'),
    url(r'^contactus/$', 'flatpage', {'url': '/contactus/'}, name='Cairo Jazz Festival - Contact Us'),
    url(r'^Artists/$', 'flatpage', {'url': '/Artists/'}, name='Cairo Jazz Festival - Artists'),
    url(r'^ourpartners/$', 'flatpage', {'url': '/ourpartners/'}, name='Cairo Jazz Festival - Out Partners'),
)