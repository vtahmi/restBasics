from rest_framework import serializers

from books_api.models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'pages', 'description', 'authors']

    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)
        authors = [author['name'] for author in authors_data]
        existing_authors = Author.objects.filter(name__in=authors)
        new_authors_names = set(authors) - set(existing_authors.values_list('name', flat=True))
        new_authors = [Author(name=name) for name in new_authors_names]
        Author.objects.bulk_create(new_authors)
        all_authors = list(existing_authors) + new_authors
        book.authors.set(all_authors)
        return book

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class PublisherHyperLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'