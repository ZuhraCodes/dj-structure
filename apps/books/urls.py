from .api_endpoints import BookList
from apps.books import api_endpoints
from django.urls import path

urlpatterns = [
    path("list/", BookList.BookListAPIView.as_view(), name="book-list"),
    path("create/", api_endpoints.BookCreateAPIView.as_view(), name="book-create"),
    path("detail/<int:pk>/", api_endpoints.BookRetrieveAPIView.as_view(), name="book-detail"),
    path("update/<int:pk>/", api_endpoints.BookUpdateAPIView.as_view(), name="book-update"),
    path("delete/<int:pk>/", api_endpoints.BookDeleteAPIView.as_view(), name="book-delete"),
]