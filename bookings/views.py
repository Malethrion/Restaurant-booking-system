from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':  # If the form is submitted
        form = UserRegistrationForm(request.POST)
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the user to the database
            return redirect('login')  # Redirect the user to the login page
    else:
        form = UserRegistrationForm()  # Display an empty form
    return render(request, 'bookings//template/register.html', {'form': form})  # Render the template

@login_required
def book_table(request):
    # Logic for booking a table
    pass
