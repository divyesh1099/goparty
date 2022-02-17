from django.db import models
from django_google_maps import fields
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = fields.AddressField(max_length=200)
    geolocation = fields.GeoLocationField(max_length=100)
    def __str__(self):
        return self.name

class RestaurantImage(models.Model):
    image = models.ImageField(upload_to = 'restaurant_images/')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="images")