from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from django.views.generic import CreateView, UpdateView
from .form import BookForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'bookshelf/login.html'
    success_url = 'view'
    

@login_required
@permission_required('bookshelf.can_view_book')
def view(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'bookshelf/list_books.html', context)

@login_required
@permission_required('bookshelf.can_create_book', raise_exception=True)
class CreateBookView(CreateView):
    form_class = BookForm
    model = Book
    template_name = 'bookshelf/create_book.html'

@login_required

@permission_required('bookshelf.can_edit_book', raise_exception=True)
class EditBookView(UpdateView):
    form_class = BookForm
    model = Book
    template_name = 'bookshelf/edit_book.html'
@login_required
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book,pk=pk)
    book.delete()
    return HttpResponse("Book deleted successfully")
