from django.test import TestCase

class Day(models.Model):
	DayName = models.CharField(max_length = 20, primary_key = True, unique = True )
	Price  = models.CharField(max_length = 8)

	pass

	def __str__(self):
		return self.DayName
	
class Show(models.Model):
	DayName = models.ForeignKey(Day)
	Artist = models.CharField(max_length = 30)
	StartTime  = models.DateTimeField(auto_now = False, auto_now_add = False)
	EndTime  = models.DateTimeField(auto_now = False, auto_now_add = False)
	

# Create your tests here.
