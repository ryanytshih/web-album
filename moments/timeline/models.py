from django.db import models

# Create your models here.
class Photo(models.Model):
    time = models.DateTimeField()
    image = models.ImageField(upload_to="photos/")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    place = models.CharField(max_length=200)
