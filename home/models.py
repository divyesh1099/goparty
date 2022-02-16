from django.db import models
from django_google_maps import fields
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = fields.AddressField(max_length=200)
    geolocation = fields.GeoLocationField(max_length=100)

    def __str__(self):
        return self.name