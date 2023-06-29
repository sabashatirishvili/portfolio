from django.contrib import admin
from .models import *

class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_time')
    search_fields = ('id', 'title')
# Register your models here.
admin.site.register(BlogPost, BlogpostAdmin)