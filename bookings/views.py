from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, ReservationForm
from .models import Reservation


# Home Page View
def index(request):
    return render(request, "bookings/index.html")


# Menu Page View
def menu(request):
    return render(request, "bookings/menu.html")


# User Registration
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Registration successful! You can now log in."
            )
            return redirect("login")
        else:
            messages.error(
                request, "Registration failed. Please correct the errors below."
            )
    else:
        form = UserRegistrationForm()
    return render(request, "bookings/register.html", {"form": form})


# User Login
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    return render(request, "bookings/login.html")


# User Logout
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect("index")


# Reservation: Create
@login_required
def create_reservation(request):
    """Handle the creation of a new reservation for authenticated users."""
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Reservation created successfully!")
            return redirect("list_reservations")
    else:
        form = ReservationForm()
    return render(request, "bookings/create_reservation.html", {"form": form})


# Reservation: List
@login_required
def list_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    if not reservations:
        messages.info(request, "You have no reservations yet.")
    else:
        messages.info(request, "Here are your current reservations.")
    return render(
        request, "bookings/list_reservations.html", {"reservations": reservations}
    )


# Reservation: Update
@login_required
def update_reservation(request, pk):
    """Handle updating an existing reservation for authenticated users."""
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation updated successfully!")
            return redirect("list_reservations")
    else:
        form = ReservationForm(instance=reservation)
    return render(request, "bookings/update_reservation.html", {"form": form})


# Reservation: Delete
@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Reservation deleted successfully.")
        return redirect("list_reservations")
    return render(request, "bookings/delete_reservation.html", {"reservation": reservation})


# Table Booking (Placeholder)
@login_required
def book_table(request):
    messages.info(request, "Table booking feature is under development.")
    return render(request, "bookings/book_table.html")
