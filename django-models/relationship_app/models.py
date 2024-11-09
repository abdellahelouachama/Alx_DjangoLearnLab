from django.db import models
from django.contrib.auth.models import User
# Create your models here
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        permissions = ('can_add_book', 'can_change_book', 'can_delete_book')
class Library(models.Model):
    name = models.CharField(max_length=100)
    Book = models.ManyToManyField(Book)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)       

class UserProfile(models.Model):
    choises_role = [{'Admin':('can_add_book', 'can_delete_book', 'can_change_book')},
                    {'Librarian':('can_add_library', 'can_delete_library', 'can_change_library')},
                    {'Member':('can_view_book', 'can_view_library')}]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=choises_role)


