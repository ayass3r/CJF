from django.shortcuts import render
from SpecialGuests.models import SpecialArtist

# Create your views here.
def specialguests(request):
    ArtistList = SpecialArtist.objects.all()
    return render(request, 'SpecialGuests/specialguests.html', {'artists':ArtistList})