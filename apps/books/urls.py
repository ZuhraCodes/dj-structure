from .api_endpoints import BookList
from .api_endpoints.BookRetrieve.views import BookRetrieveAPIView
from django.urls import path

urlpatterns = [
    path("list/", BookList.BookListAPIView.as_view(), name="book-list"),
    path("detail/<int:pk>/", BookRetrieveAPIView.as_view(), name="book-detail")
]