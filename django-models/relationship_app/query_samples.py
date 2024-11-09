from models import Author, Book, Library, Librarian

books = Book.objects.get(author='John Doe')
Library.objects.get(name = "My Library").Book.all()
Librarian.objects.get(library = "my library").name
