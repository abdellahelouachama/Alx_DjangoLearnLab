from django.urls import path
from .views import ListView, CreateView, UpdateView, DetailView, DeleteView
from rest_framework.authtoken import views


urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('books/', ListView.as_view()),
    path('books/<int:pk>/', DetailView.as_view()),
    path('books/create/', CreateView.as_view()),
    path('books/Update<int:pk>/', UpdateView.as_view()),
    path('books/delete/<int:pk>/', DeleteView.as_view())

]