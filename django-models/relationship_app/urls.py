from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/',list_books, name='list_books'),
    path('library detail/<int:library_id>', LibraryDetailView, name='library_detail'),
]