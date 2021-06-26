from django.db import models

# Create your models here.
class EmailEntry(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120,blank=True)
    Bio = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True) # set when saved?
    timestamp = models.DateTimeField(auto_now_add=True) # set wen add 