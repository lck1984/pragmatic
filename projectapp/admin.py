from django.contrib import admin

# Register your models here.
from projectapp.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'created_at')

