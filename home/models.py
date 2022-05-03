from pyexpat import model
from statistics import mode
from django.db import models
from django_google_maps import fields
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = fields.AddressField(max_length=200)
    geolocation = fields.GeoLocationField(max_length=100)
    price = models.IntegerField(default=1000, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    edited = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created = models.DateTimeField(auto_now=True, blank=True, null=True)
    

    def __str__(self):
        return self.name

class RestaurantImage(models.Model):
    image = models.ImageField(upload_to = 'restaurant_images/')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="images")

class RestaurantFeature(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name="features")
    great_food = models.BooleanField(default=True)
    satisfactory_staff = models.BooleanField(default=True)
    great_ambience = models.BooleanField(default=True)
    good_service = models.BooleanField(default=True)
    resonable_cost = models.BooleanField(default=True)
    hygiene_and_cleanliness = models.BooleanField(default=True)

    def __str__(self):
        return self.restaurant.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'user/profile/default_user.jpg', upload_to = 'user/profile/%Y/%m/%d/')
    
    def __str__(self):
        return self.user.username

class Featured(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="featureds")

    def __str__(self):
        return self.restaurant.name