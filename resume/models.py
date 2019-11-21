from django.db import models

class Job(models.Model):
	"""Model for rendering past Jobs"""

	title = models.CharField(max_length=50)
	company = models.CharField(max_length=50)
	start_date = models.DateField()
	end_date = models.DateField()
	current = models.BooleanField()
	description = models.TextField()
