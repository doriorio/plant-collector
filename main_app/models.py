from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Pollinator(models.Model):
    name = models.CharField(max_length=140)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('pollinators_detail', kwargs={'pk': self.id})
    

class Plant(models.Model):
    species = models.CharField(max_length=140)
    common_name = models.CharField(max_length=140)
    color = models.CharField(max_length=140)
    native_location = models.CharField(max_length=140)
    description = models.CharField(max_length=480, default="")
    pollinators = models.ManyToManyField(Pollinator)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})


TYPES = (
    ('C', "Culinary"),
    ('H', "Homeopathic"),
    ('T', "Topical"),
    ('A', "Aromatic"),
    ('M', "Medicinal"),
)


class Use(models.Model):
    primary_type = models.CharField(
        max_length=1,
        choices=TYPES
    )
    description = models.CharField(max_length=480, default="")
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.description} is a plant used for {self.get_primary_type_display()} purposes')