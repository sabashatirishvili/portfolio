from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=30)
  description = models.TextField(max_length=90)
  logo_url = models.FilePathField(path='media/project_logos/')

class Technology(models.Model):
  name = models.CharField(max_length=25)
  logo_url = models.FilePathField(path='media/technology_logos/')

