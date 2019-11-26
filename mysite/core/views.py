from django.shortcuts import render
from .models import Passenger


# Create your views here.


def landing_view(request):
    return render(request, 'index.html')

def driver_view(request):
    return render(request, 'driver_view.html')

def rider_view(request):
    return render(request, 'rider_view.html')

def verification_view(request):
    return render(request, 'verification.html')

