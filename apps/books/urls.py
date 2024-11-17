from .api_endpoints import BookList
from apps.books import api_endpoints
from .api_endpoints.BookUpdate import BookUpdateAPIView
from django.urls import path

urlpatterns = [
    path("list/", BookList.BookListAPIView.as_view(), name="book-list"),
    path("detail/<int:pk>/", api_endpoints.BookRetrieveAPIView.as_view(), name="book-detail"),
    path("update/<int:pk>/", BookUpdateAPIView.as_view(), name="book-update"),
]