from models import Author, Book, Library, Librarian

books = Book.objects.get(author='John Doe')
Library.objects.get(name = "library_name").book.all()
Librarian.objects.get(library = 'library_name').Library.all()
# Library.objects.get(name=library_name).books.all()
# Author.objects.get(name=author_name).objects.filter(author=author)
# Librarian.objects.get(library = library_name)
# Librarian.objects.get(library=