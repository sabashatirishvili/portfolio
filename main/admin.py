from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'image_static_url', 'display_technologies')
  filter_horizontal = ('technologies',)
  search_fields = ('title',)

  def display_technologies(self, obj):
        return ", ".join([technology.name for technology in obj.technologies.all()])


class TechnologyAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'category')
  search_fields = ('name',)

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)

