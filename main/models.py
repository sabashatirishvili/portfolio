from django.db import models

# Create your models here.
class Technology(models.Model):
  THREE_CATEGORIES = (
    ('frontend', "Front-end"),
    ('backend', "Back-end"),
    ('misc', "Miscellaneous"),
  )
  
  name = models.CharField(max_length=25)
  category = models.CharField(
    max_length=15,
    choices = THREE_CATEGORIES,
    default= 'frontend')
  
  def __str__ (self):
    return self.name
  

class Project(models.Model):
  title = models.CharField(max_length=40)
  description = models.TextField(max_length=200)
  image_static_url = models.CharField(max_length=225, null=True)
  github_link = models.URLField(max_length=100)
  website_link = models.URLField(max_length=100)
  technologies = models.ManyToManyField(Technology)

  def __str__ (self):
    return self.title
