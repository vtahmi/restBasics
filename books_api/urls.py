from django.urls import path
from rest_framework.routers import DefaultRouter

from books_api.views import create_book, BookViewSet, BookList, PublisherViewSet, PublisherHyperLinkView

router = DefaultRouter()
router.register(r'publishers', PublisherViewSet)
urlpatterns = [
    path("<int:pk>/", BookViewSet.as_view(), name="book"),
    path("create/", create_book, name="create-book"),
    path("", BookList.as_view(), name="book-list"),
    *router.urls,
    path("publishers-link/", PublisherHyperLinkView.as_view(), name="publisher-hyperlink"),
]
