from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library detail/<int:library_id>', views.LibraryDetail, name='library_detail'),
]