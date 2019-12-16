from django.db import models
from django.urls import reverse

# Create your models here.
class Plant(models.Model):
    species = models.CharField(max_length=140)
    common_name = models.CharField(max_length=140)
    color = models.CharField(max_length=140)
    native_location = models.CharField(max_length=140)
    description = models.CharField(max_length=480, default="")
    isHousePlant = models.BooleanField

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})