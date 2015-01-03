from django.shortcuts import render
from LineUp.models import Artist

# Create your views here.
def index(request):
    artistList = Artist.objects.all().order_by('ArtistName')
    return render(request, 'LineUp/index.html', {'artists':artistList})