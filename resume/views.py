from django.shortcuts import render
from .models import Job
from projects.models import Project

def home(request):
	jobs = Job.objects
	projects = Project.objects
	return render(request, 'resume/home.html', {'jobs':jobs, 'projects':projects})
