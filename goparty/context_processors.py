from home.models import *

def getcities(request):
    cities = list()
    try:
        restaurant_list = Restaurant.objects.all()
        for restaurant in restaurant_list:
            if restaurant.city in cities:
                pass
            else: 
                cities.append(restaurant.city)
        return {
            "cities":cities,
        }
    except :
        return []