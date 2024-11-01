from bookshelf.models import Book
obj = Book.objects.get(title="1984")
obj.title = "Nineteen Eighty-Four"
obj.save()
# Nineteen Eighty-Four     