from rest_framework import serializers
from .models import Book, Author
import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'publication_year', 'author')

    def validate_publication_year(self, value):
        current_year = datetime.datetime.today().year   

        if value > current_year: 
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True) 

    class Meta:
        model = Author
        fields = '__all__'

# AuthorSerializer and BookSerializer are defined to convert Author and Book objects to JSON format and vice versa
