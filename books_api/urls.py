from django.urls import path

from books_api.views import create_book, BookViewSet, BookList

urlpatterns = [
    path("<int:pk>", BookViewSet.as_view(), name="book"),
    path("create", create_book, name="create_book"),
    path("", BookList.as_view(), name="book_list"),
]
