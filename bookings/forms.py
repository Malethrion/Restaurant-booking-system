from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Reservation


class UserRegistrationForm(UserCreationForm):
    pass  # default fields (username, password, confirm password)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'date', 'time', 'guests', 'contact_email']
