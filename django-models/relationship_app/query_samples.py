from models import Author, Book, Library, Librarian

books = Book.objects.get(author='John Doe')
library_books = Library.objects.get(name = "My Library").Book.all()
librarian = Librarian.objects.get(library = "my library").name
