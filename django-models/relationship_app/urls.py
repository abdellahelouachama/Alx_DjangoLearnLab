from django.urls import path
from . import views


urlpatterns = [
    path('book list', views.list_books_view, name='list_books'),
    path('library detail <int:library_id>', views.LibraryDetailView, name='library_detail'),
   
]