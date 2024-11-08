from models import Author, Book, Library, Librarian

books = Book.objects.select_related('author').get(id=1)
Library_books = Library.objects.prefetch_related('boks').all()
Librarian_library = Librarian.objects.select_related('library').all()
