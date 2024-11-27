from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Map the registration view to the /register/ URL
]
