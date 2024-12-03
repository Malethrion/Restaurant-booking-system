from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, ReservationForm
from .models import Reservation

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
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email verification
            user.save()
            
            # Generate email verification token
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = f"http://{current_site.domain}/activate/{uid}/{token}/"

            # Render email content
            message = render_to_string('bookings/email_verification.html', {
                'user': user,
                'activation_link': activation_link,
            })

            # Send email
            email = EmailMessage(mail_subject, message, to=[user.email])
            email.send()

            return render(request, 'bookings/registration_complete.html')
    else:
        form = UserRegistrationForm()  # Display an empty form
    return render(request, 'bookings/register.html', {'form': form})  # Render the template

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)  # Log the user in after activation
        return redirect('index')  # Redirect to home page after successful activation
    else:
        return render(request, 'bookings/activation_invalid.html')

@login_required
def book_table(request):
    # Logic for booking a table
    pass

def menu(request):
    return render(request, 'menu.html')

# Render email content
message = render_to_string('bookings/email/email_verification.html', {
    'user': user,
    'activation_link': activation_link,
})
