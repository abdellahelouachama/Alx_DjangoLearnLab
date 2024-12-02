from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser

 
def register(request):
    """
Handles user registration by displaying and processing a registration form.

If the request method is POST, it validates the form data and saves a new user
if the data is valid. Upon successful registration, redirects the user to the 
login page. If the request method is not POST, it initializes an empty 
registration form. Renders the registration page with the form.

Args:
    request: The HTTP request object.

Returns:
    HttpResponse: Renders the registration page with the form.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form':form})    


class LoginView(LoginView):
    """
Handles user login by displaying and processing a login form. 
    """
    template_name = 'registration/login.html'
    form_class = AuthenticationForm  

class LogoutView(LogoutView):
    """
Handles user logout by destroying the user's session.
    """
    template_name = 'registration/logout.html'
    next_page = '/login'

@login_required
def profile(request):
    """
    Handles the user profile update by displaying and processing a profile form.

    If the request method is POST, it validates and updates the user's data using
    the provided form. Upon successful update, it redirects the user to the profile
    page. If the request method is not POST, it initializes the form with the current
    user's data. Renders the profile page with the form.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the profile page with the form.
    """
    
    # Get the current user
    user = request.user

    # If the request method is POST, process the form
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)  # Use the form to update the user's data
        if form.is_valid():
            form.save()  # Save the updated data to the database
            return redirect('profile')  # Redirect to the profile page after successful update
    else:
        form = CustomUserChangeForm(instance=user)  # Render the form with current user data

    return render(request, 'profile.html', {'form': form})