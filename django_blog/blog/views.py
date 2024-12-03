from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, PostCreateForm, PostUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Post
# Authentication views  
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
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form':form})    

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

    return render(request, 'blog/profile.html', {'form': form})

# home view for displaying the menu
def home(request):
    """
Renders the home page of the blog application.

This view function handles the HTTP request for the home page and returns an 
HttpResponse object that renders the 'home.html' template.

Args:
    request: The HTTP request object.

Returns:
    HttpResponse: Renders the home page template.
     """
    return render(request, 'blog/home.html')
# Plog post views
class ListView(ListView):
    model = Post
    template_name = 'blog/list.html'

class DetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

@login_required
class CreatView(CreateView):
    model = Post
    template_name = 'blog/create.html'
    form_class = PostCreateForm
    success_url = 'home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Post
    template_name = 'blog/update.html'
    form_class = PostUpdateForm
    success_url = 'home'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class DeleteView(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
    model = Post
    template_name = 'blog/delete.html'
    success_url = 'home'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
       
    
