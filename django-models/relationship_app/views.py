from django.shortcuts import render
from django.views.generic import ListView
from . models import Author, Book, Library, Librarian
from .models import Library
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "relationship_app/list_books.html.html", context)

class LibraryDetail(ListView):
    model = Library
    template_name = "relationship_app/library_detail.html.html"

 