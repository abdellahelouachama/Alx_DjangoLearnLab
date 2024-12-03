from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Post, Comment
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
    form_class = PostForm
    success_url = 'home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Post
    template_name = 'blog/update.html'
    form_class = PostForm
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
       
    
# comment views for crud operations
# view to list all comments
class ListViewComment(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'

# view to create comment under post
@login_required
class CreatViewComment(CreateView):
    model = Comment
    template_name = 'blog/comment_create.html'
    form_class = CommentForm

    def form_valid(self, form):
        # Extract post_id from the URL
        post_id = self.kwargs['post_id']
        # Get the post instance
        post = get_object_or_404(Post, id=post_id)
        # Associate the comment with the logged-in user and the post
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)

# update comment 
class UpdateViewComment(UpdateView, UserPassesTestMixin, LoginRequiredMixin):    
    model = Comment
    template_name = 'blog/comment_update.html'
    form_class = CommentForm

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

# delete comment
class DeleteViewComment(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Comment
    template_name = 'blog/comment_update.html'
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
