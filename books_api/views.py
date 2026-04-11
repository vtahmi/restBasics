from django.http import JsonResponse

from books_api.models import Book


def book(request):
    book = Book.objects.get(pk=1)

    return JsonResponse({"message": "Hello, World!"})
