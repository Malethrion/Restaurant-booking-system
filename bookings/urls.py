from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('', views.index, name='index'),  # Root URL for the bookings app
    path('register/', views.register, name='register'),  # Registration URL
    path('reservations/', views.list_reservations, name='list_reservations'),  # Reservations list
    path('reservations/new/', views.create_reservation, name='create_reservation'),  # Create reservation
    path('reservations/<int:pk>/edit/', views.update_reservation, name='update_reservation'),  # Update reservation
    path('reservations/<int:pk>/delete/', views.delete_reservation, name='delete_reservation'),  # Delete reservation
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
