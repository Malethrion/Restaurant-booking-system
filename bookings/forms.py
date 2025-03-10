from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from datetime import datetime, date


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["customer_name", "date", "time", "guests", "contact_email"]
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "YYYY-MM-DD",
                }
            ),
            "time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "placeholder": "HH:MM",
                }
            ),
        }
        help_texts = {
            "date": "Please use the format YYYY-MM-DD (future dates only).",
            "time": (
                "Please use the format HH:MM (restaurant hours: 11:00–22:00)."
            ),
        }

    contact_email = forms.EmailField(
        validators=[
            EmailValidator(
                message="Enter a valid email address (e.g., user@example.com)."
            )
        ],
        required=True,
    )

    def clean_date(self):
        date_value = self.cleaned_data["date"]
        if date_value < date.today():
            raise ValidationError("Reservations can't be made for past dates.")
        return date_value

    def clean_guests(self):
        guests = self.cleaned_data["guests"]
        if guests <= 0:
            raise ValidationError("Number of guests must be positive.")
        return guests

    def clean_contact_email(self):
        email = self.cleaned_data["contact_email"]
        validator = EmailValidator(
            message="Enter a valid email address (e.g., user@example.com)."
        )
        validator(email)
        return email

    def clean_time(self):
        time_value = self.cleaned_data["time"]
        restaurant_open = datetime.strptime("11:00", "%H:%M").time()
        restaurant_close = datetime.strptime("22:00", "%H:%M").time()
        if time_value < restaurant_open or time_value > restaurant_close:
            raise ValidationError("Reservations must be between 11:00 and 22:00.")
        return time_value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["contact_email"].validators = [
            EmailValidator(
                message="Enter a valid email address (e.g., user@example.com)."
            )
        ]
