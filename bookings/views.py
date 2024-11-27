from django.shortcuts import render
from .forms import UserRegistrationForm  # Importing form

def register(request):
    if request.method == 'POST':  # If the form is submitted
        form = UserRegistrationForm(request.POST)
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the user to the database
            return redirect('login')  # Redirect the user to the login page
    else:
        form = UserRegistrationForm()  # Display an empty form
    return render(request, 'register.html', {'form': form})  # Render the template