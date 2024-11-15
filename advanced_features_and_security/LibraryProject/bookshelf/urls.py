from django.urls import path
from . import views

app_name = 'bookshelf'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('view', views.view, name='book_list'),
    path('create/', views.CreateBookView, name='create_book'),
    path('<int:pk>/edit/', views.EditBookView, name='edit_book'),
    path('<int:pk>/delete/', views.delete_book, name='delete_book'),
]