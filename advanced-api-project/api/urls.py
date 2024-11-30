from django.urls import path
from .views import ListView, CreateView, UpdateView, DetailView, DeleteView
from rest_framework.authtoken import views


urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('books/', ListView.as_view()),
    path('books/<int:pk>/', DeleteView.as_view()),
    path('books/', CreateView.as_view()),
    path('books/<int:pk>/', UpdateView.as_view()),
    path('books/<int:pk>/', DeleteView.as_view())

]