from django.db import models



class Youtube(models.Model):
	VideoTitle = models.CharField(max_length = 100)
	VideoLink = models.URLField(max_length = 300)

	def __str__(self):
		return self.VideoTitle

class SoundCloud(models.Model):
	SoundTitle = models.CharField(max_length = 100)
	SoundLink = models.URLField(max_length = 300)

	def __str__(self):
		return self.SoundTitle

class EventPicture(models.Model):
	EventPictureTitle = models.CharField(max_length = 100)
	EventPictureUpload = models.ImageField(upload_to = 'EventPictureImages')
	
	def __str__(self):
		return self.EventPictureTitle