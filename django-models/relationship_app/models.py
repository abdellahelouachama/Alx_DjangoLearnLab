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
class Library(models.Model):
    name = models.CharField(max_length=100)
    Book = models.ManyToManyField(Book)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)       

class UserProfile(models.Model):
    choises_role = ['Admin', 'Librarian', 'Member']
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=choises_role)