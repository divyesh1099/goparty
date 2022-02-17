from django.contrib import admin
from django_google_maps import widgets
from django_google_maps import fields
from .models import *
# Register your models here.
class RestaurantImageInline(admin.StackedInline):
    model = RestaurantImage

class RestaurantAdmin(admin.ModelAdmin):
    formfield_overrides = {
        fields.AddressField:{'widget':widgets.GoogleMapsAddressWidget},
    }
    inlines = [
        RestaurantImageInline,
    ]


admin.site.register(Restaurant, RestaurantAdmin)