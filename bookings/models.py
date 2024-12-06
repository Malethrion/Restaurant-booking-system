from django.db import models
from django.contrib.auth.models import User

# Reservation model: Stores booking details such as date, time, and customer info.
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)  # Name of the person making the reservation
    date = models.DateField()  # Date of the reservation
    time = models.TimeField()  # Time of the reservation
    guests = models.IntegerField()  # Number of guests
    contact_email = models.EmailField()  # Contact email for the reservation
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# FAQ model: Stores frequently asked questions and their answers for the FAQ page.
class FAQ(models.Model):
    question = models.CharField(max_length=200)  # Question text
    answer = models.TextField()  # Answer text