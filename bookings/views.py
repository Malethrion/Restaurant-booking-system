from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required


@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_reservations')  # Redirect to a list of reservations
    else:
        form = ReservationForm()
    return render(request, 'bookings/create_reservation.html', {'form': form})


def list_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'bookings/list_reservations.html', {'reservations': reservations})


def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('list_reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'bookings/update_reservation.html', {'form': form})


def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('list_reservations')
    return render(request, 'bookings/delete_reservation.html', {'reservation': reservation})


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
