from django.db import models

class Project(models.Model):
	"""Model for rendering project overviews"""
	
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)
