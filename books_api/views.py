from django.db.migrations import serializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from books_api.models import Book, Publisher
from books_api.serializers import BookSerializer, PublisherSerializer, PublisherHyperLinkSerializer


# def book(request):
#     book = Book.objects.get(pk=1)
#
#     return JsonResponse({
#         'title': book.title,
#         'pages': book.pages,
#         'description': book.description,
#         'author': book.author})

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # better option is Book.objects.prefetch_related('authors')
    serializer_class = BookSerializer

class BookViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookView(APIView):
#     serializer = BookSerializer
#     def get_object(self, pk):
#         return get_object_or_404(Book, pk=pk)
#
#     def get(self, request, pk):
#         book = self.get_object(pk)
#         serializer = self.serializer(book)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     def put(self, request, pk):
#         book = self.get_object(pk)
#         serializer = self.serializer(instance=book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def patch(self, request, pk):
#         book = self.get_object(pk)
#         serializer = self.serializer(instance=book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_200_OK)
# @api_view(['GET'])
# def book(request, pk):
#     book = Book.objects.get(pk=pk)
#     serializer = BookSerializer(book)
#     return Response(serializer.data)

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherHyperLinkView(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherHyperLinkSerializer
