from django.db import models

class Picture(models.Model):
		
		PictureTitle = models.CharField(max_length = 50)
		CarasoulPicture = models.ImageField(upload_to = 'CarouselImages')
		PictureLink = models.URLField(max_length = 500)

		def __str__(self):
			return self.PictureTitle
