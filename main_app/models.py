from django.db import models

# Create your models here.
class Plant(models.Model):
    species = models.CharField(max_length=140)
    common_name = models.CharField(max_length=140)
    color = models.CharField(max_length=140)
    native_location = models.CharField(max_length=140)
    description = models.CharField(max_length=480, default="")
    isHousePlant = models.BooleanField