from django.contrib import admin
from .models import Tag, Project

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_filter = ['tag']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "date"]
    list_filter = ["title"]


admin.site.register(Tag)
admin.site.register(Project, ProjectAdmin)
