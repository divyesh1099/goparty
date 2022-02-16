from django.shortcuts import render
from .models import *
import json
# Create your views here.
def index(request):
    location_list = list(Location.objects.order_by('name').values())
    context = {'location_list': location_list}
    return render(request, 'home/index.html', context)