from models import Author, Book, Library, Librarian

books = Book.objects.select_related('author').get(id=1)
Library.objects.get(name='library_name')
Librarian.objects.select_related('library').all()
