# bookings/models.py
from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    contact_email = models.EmailField()

    def __str__(self):
        return f"{self.customer_name} - {self.date} {self.time}"


class FAQ(models.Model):
    question = models.CharField(max_length=200)  # Question text
    answer = models.TextField()  # Answer text
