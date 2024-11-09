from django.urls import path
from .views import list_books

urlpatterns = [
    path('book list',list_books, name='list_books'),
    path('library detail <int:library_id>', LibraryDetailView, name='library_detail'),
   
]