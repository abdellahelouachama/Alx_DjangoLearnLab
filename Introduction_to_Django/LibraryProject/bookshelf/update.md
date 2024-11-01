obj = Book.objects.title("1984")
obj.title = "Nineteen Eighty-Four"
obj.save()
# Nineteen Eighty-Four     