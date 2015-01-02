from django.contrib import admin

from PreviousEvents.models import Youtube, SoundCloud, EventPicture

admin.site.register(Youtube)

admin.site.register(SoundCloud)

admin.site.register(EventPicture)
