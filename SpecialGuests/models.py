from django.db import models


class SpecialArtist(models.Model):
	ArtistName = models.CharField(max_length = 30)
	ArtistInfo = models.CharField(max_length = 1000)
	PlaceOfOrigin = models.CharField(max_length = 100)
	YearsRunning = models.CharField(max_length = 20)
	ArtistsImage = models.ImageField(upload_to = 'SpecialGuestImages') #Edit the directory of saved pictures on server
	ArtistTwitter = models.URLField(max_length = 300)
	ArtistFacebook = models.URLField(max_length = 300)

	def __str__(self):
		return self.ArtistName


