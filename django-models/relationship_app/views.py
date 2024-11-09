from django.shortcuts import render
from django.views.generic import ListView
from . models import Book
from .models import Library
# Create your views here
def list_books_view(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(ListView):
    model = Library

    def specific_library(self, request, library_name):
        library = Library.objects.filter(name=library_name)
        context = {
            'library' : library
        }
        return render(request, 'relationship_app/library_detail.html', context)