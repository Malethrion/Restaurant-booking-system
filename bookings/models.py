from django.db import models

# Reservations
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)  # Name of the person making the reservation
    date = models.DateField()  # Date of the reservation
    time = models.TimeField()  # Time of the reservation
    guests = models.IntegerField()  # Number of guests
    contact_email = models.EmailField()  # Contact email for the reservation

# FAQ
class FAQ(models.Model):
    question = models.CharField(max_length=200)  # Question text
    answer = models.TextField()  # Answer text