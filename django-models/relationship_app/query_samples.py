from models import Author, Book, Library, Librarian

books = Book.objects.select_related('author').get(id=1)
Library.objects.get(name=library_name)
books.all()
Author.objects.get(name=author_name)
objects.filter(author=author)
Librarian.objects.get(library=library)