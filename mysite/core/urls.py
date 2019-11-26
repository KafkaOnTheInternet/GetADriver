from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_view),
    path('driver', views.driver_view),
    path('rider', views.rider_view),
    path('auth', views.verification_view)
]