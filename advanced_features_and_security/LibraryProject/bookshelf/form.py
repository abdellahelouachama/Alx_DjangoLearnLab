from django.contrib.auth.forms import UserCreationForm
from .models import Book


class BookForm(UserCreationForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

