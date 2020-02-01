from django.db import models
import datetime

class Project(models.Model):
	"""Model for rendering project"""
	
	image = models.ImageField(upload_to='images/')
	tile = models.CharField(max_length=100, default="Project Name")
	tech_stack = models.CharField(max_length=200)
	start_date = models.DateField(default=datetime.date.today)

	class Meta:
		ordering = ["-start_date"]