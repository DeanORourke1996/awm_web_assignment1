from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Locations(models.Model):
    name = models.CharField('Name', max_length=90)
    country = models.CharField('Country', max_length=50)
    rating = models.DecimalField('Rating', max_digits=2, decimal_places=1)
    lon = models.FloatField('Longitude')
    lat = models.FloatField('Latitude')

    def __str__(self):
        return self.name
