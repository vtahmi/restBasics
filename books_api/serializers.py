from rest_framework import serializers

from books_api.models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'pages', 'description', 'authors']
