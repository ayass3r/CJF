from django.db import models


class Artist(models.Model):
	ArtistName = models.CharField(max_length = 30)
	ArtistInfo = models.CharField(max_length = 500)
	PlaceOfOrigin = models.CharField(max_length = 100)
	YearsRunning = models.CharField(max_length = 20)
	ArtistsImage = models.ImageField(upload_to = 'LineupImages') #Edit the directory of saved pictures on server
	ArtistTwitter = models.URLField(max_length = 300)
	ArtistFacebook = models.URLField(max_length = 300)

	def __str__(self):
		return self.ArtistName

# Create your models here.
