from django.shortcuts import render
from Carousel.models import Picture

# Create your views here.
def home(request):
	CarouselList = Picture.objects.all()
	return render( request, 'Carousel/home.html' , {'HomeCarousel':CarouselList})
