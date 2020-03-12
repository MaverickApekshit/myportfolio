from django.db import models
import datetime

class Project(models.Model):
	"""Model for rendering project"""
	
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100, default="Project Name")
	tech_stack = models.CharField(max_length=200)
	github_link = models.URLField(max_length=500, blank=True)
	demo_link = models.URLField(max_length=500, blank=True)
	start_date = models.DateField(default=datetime.date.today)
	discription = models.TextField(default="Project Description")

	class Meta:
		ordering = ["-start_date"]

	def __str__(self):
		return self.title