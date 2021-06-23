from django.db import models

# Create your models here.

class Restaurant(models.Model):
    google_place_id = models.CharField(max_length=16)
    icon = models.CharField(max_length=256,null=True)
    rating = models.CharField(max_length=4,null=True)
    name = models.CharField(max_length=256)
