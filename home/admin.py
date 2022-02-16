from django.contrib import admin
from django_google_maps import widgets
from django_google_maps import fields
from .models import *
# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        fields.AddressField:{'widget':widgets.GoogleMapsAddressWidget},
    }

admin.site.register(Location, LocationAdmin)