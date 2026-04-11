from django.urls import path

from books_api.views import book

urlpatterns = [
    path("", book, name="book")
]
