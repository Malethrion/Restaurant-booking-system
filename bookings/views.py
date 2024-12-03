from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login, authenticate
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
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email verification
            user.save()

            # Send verification email
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = f"http://{current_site.domain}/activate/{uid}/{token}/"

            message = render_to_string('bookings/email_verification.html', {
                'user': user,
                'activation_link': activation_link,
            })

            email = EmailMessage(mail_subject, message, to=[user.email])
            email.send()

            return render(request, 'bookings/registration_complete.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'bookings/register.html', {'form': form})


# Account Activation
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'bookings/activation_invalid.html')


# Reservation: Create
@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Associate with the logged-in user
            reservation.save()
            return redirect('list_reservations')
    else:
        form = ReservationForm()
    return render(request, 'bookings/create_reservation.html', {'form': form})


# Reservation: List
@login_required
def list_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)  # Show only user's reservations
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
