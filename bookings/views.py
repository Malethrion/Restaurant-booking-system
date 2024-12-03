from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ReservationForm
from .models import Reservation

# Home Page View
def index(request):
    return render(request, 'bookings/index.html')

# Menu Page View
def menu(request):
    return render(request, 'bookings/menu.html')

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'bookings/register.html', {'form': form})

# Reservation: Create
@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('list_reservations')
    else:
        form = ReservationForm()
    return render(request, 'bookings/create_reservation.html', {'form': form})

# Reservation: List
@login_required
def list_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'bookings/list_reservations.html', {'reservations': reservations})

# Reservation: Update
@login_required
def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('list_reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'bookings/update_reservation.html', {'form': form})

# Reservation: Delete
@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('list_reservations')
    return render(request, 'bookings/delete_reservation.html', {'reservation': reservation})

# Table Booking (Placeholder)
@login_required
def book_table(request):
    # Logic for table booking (placeholder)
    return render(request, 'bookings/book_table.html')

