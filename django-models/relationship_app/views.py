from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Library, Book
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "relationship_app/list_books.html.html", context)

class LibraryDetailView(ListView):
    model = Library
    template_name = "relationship_app/library_detail.html.html"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ("index")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})