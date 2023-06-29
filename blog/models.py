from django.db import models
from django.utils import timezone 

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=150)
    upload_time = models.DateTimeField(default=timezone.now)
