from models import Author, Book, Library, Librarian

books = Book.objects.get(author='John Doe')
Library.objects.get(name = "library_name").Book.all()
Librarian.objects.get(library = "library_name").name
