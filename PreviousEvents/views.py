from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import render
from PreviousEvents.models import Youtube#, SoundCloud, EventPicture

def index(request):
	youtubelist = Youtube.objects.all().order_by('VideoTitle')
	template = loader.get_template('PreviousEvents/index.html')
	context = RequestContext(request, {'youtubelist': youtubelist,})
	return HttpResponse(template.render(context))
	#soundcloudlist = SoundCloud.all()
	#eventpicturelist = EventPicture.all()
    #return render(request, 'PreviousEvents/index.html', {'youtube' :youtubelist})

