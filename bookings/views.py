from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation


def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_reservations')  # Redirect to a list of reservations
    else:
        form = ReservationForm()
    return render(request, 'bookings/create_reservation.html', {'form': form})


def index(request):
    return render(request, 'bookings/index.html')  # Render the index.html template


def register(request):
    if request.method == 'POST':  # If the form is submitted
        form = UserRegistrationForm(request.POST)
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the user to the database
            return redirect('login')  # Redirect the user to the login page
    else:
        form = UserRegistrationForm()  # Display an empty form
    return render(request, 'bookings/register.html', {'form': form})  # Render the template

@login_required
def book_table(request):
    # Logic for booking a table
    pass
