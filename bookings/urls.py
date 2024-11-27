from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL for the bookings app
    path('register/', views.register, name='register'),  # Registration URL
    path('reservations/', views.list_reservations, name='list_reservations'),  # Reservations list
    path('reservations/new/', views.create_reservation, name='create_reservation'),  # Create reservation
    path('reservations/<int:pk>/edit/', views.update_reservation, name='update_reservation'),  # Update reservation
    path('reservations/<int:pk>/delete/', views.delete_reservation, name='delete_reservation'),  # Delete reservation
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login view
]
