from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Library, Book
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

 