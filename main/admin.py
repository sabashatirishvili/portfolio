from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'image_static_url')
  search_fields = ('title',)

class TechnologyAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  search_fields = ('name',)

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)

