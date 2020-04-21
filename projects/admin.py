from django.contrib import admin

from .models import Project
from .models import ProjectImages

class ProjectImageInline(admin.TabularInline):
    model = ProjectImages
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ ProjectImageInline, ]

admin.site.register(Project, ProjectAdmin)
