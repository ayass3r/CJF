from django.db import models

class Picture(models.Model):
		
		PictureTitle = models.CharField(max_length = 50)
		CarasoulPicture = models.ImageField(upload_to = 'CarouselImages')

		def __str__(self):
			return self.PictureTitle
