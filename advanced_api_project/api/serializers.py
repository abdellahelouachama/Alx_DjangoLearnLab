from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, data):
        current_year = datetime.datetime.today().year
        
        if data['publication_year'] > current_year:
            raise serializers.ValidationError('Book cannot be published in the future')
        return data    

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = "__all__"

# Serializer for Author and Book to convert data to JSON format and vice versa