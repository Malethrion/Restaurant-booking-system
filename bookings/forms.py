from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Reservation

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'date', 'time', 'guests', 'contact_email']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'YYYY-MM-DD',
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'placeholder': 'HH:MM',
            }),
        }
        help_texts = {
            'date': 'Please use the format YYYY-MM-DD.',
            'time': 'Please use the format HH:MM.',
        }
