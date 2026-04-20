from rest_framework.permissions import BasePermission

from books_api.models import Book


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj: Book):
        author_names = obj.authors.values_list('name', flat=True)
        return request.user.username in author_names
