from django.shortcuts import render
from .models import *
import json
# Create your views here.
def index(request):
    restaurant_list = Restaurant.objects.all()
    context = {'restaurant_list':restaurant_list}
    return render(request, 'home/index.html', context)