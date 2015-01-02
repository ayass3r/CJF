from django.db import models

class Email(models.Model):
	e_mail = models.EmailField(max_length = 254) #RFC Compatibility
	
