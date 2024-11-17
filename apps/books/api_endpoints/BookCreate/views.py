from rest_framework.generics import CreateAPIView
from .serializers import BookCreateModelSerializer
from apps.books.models import Book
from rest_framework import permissions

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateModelSerializer
    permission_classes = (permissions.IsAuthenticated,)