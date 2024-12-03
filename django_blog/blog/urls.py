from django.urls import path
from django.contrib.auth import views as auth_views  # Importing built-in views
from . import views

urlpatterns = [
    # Login view
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    # Logout view (it will automatically redirect to home page or can be specified)
    path('logout/', auth_views.LogoutView.as_view(next_page='login/'), name='logout'),
    # Register view (uses your custom registration view)
    path('register/', views.register, name='register'),
    # Profile view (uses your custom profile view)
    path('profile/', views.profile, name='profile'),
    # Home view 
    path('home/', views.home, name='home'),
    # List posts view
    path('posts/', views.ListView, name='posts'),
    # Detail post view
    path('posts/<int:pk>/', views.DetailView, name='post-detail'),
    # Create post view
    path('posts/new/ ', views.CreatView, name='post-create'),
    # Edit post view
    path('posts/<int:pk>/edit/', views.UpdateView, name='post-edit'),
    # Delete post view
    path('posts/<int:pk>/delete/', views.DeleteView, name='post-delete'),
]
