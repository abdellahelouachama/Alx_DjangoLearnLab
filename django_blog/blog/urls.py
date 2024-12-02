from django.urls import path
from django.contrib.auth import views as auth_views  # Importing built-in views
from . import views

urlpatterns = [
    # Login view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Logout view (it will automatically redirect to home page or can be specified)
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    # Register view (uses your custom registration view)
    path('register/', views.register, name='register'),
    # Profile view (uses your custom profile view)
    path('profile/', views.profile, name='profile'),
]
