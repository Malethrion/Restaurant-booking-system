from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL for the bookings app
    path('register/', views.register, name='register'),  # Registration URL
]
