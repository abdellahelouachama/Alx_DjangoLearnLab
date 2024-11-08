from models import Author, Book, Library, Librarian

books = Book.objects.select_related('author').get(id=1)
Library.objects.get(name=library_name)
books.all()
Librarian.objects.select_related('library').all()
