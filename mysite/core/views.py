from django.shortcuts import render
from .models import Passenger
from django.contrib.generic

# Create your views here.


def landing_view(request):
    return render(request, 'landing.html')


