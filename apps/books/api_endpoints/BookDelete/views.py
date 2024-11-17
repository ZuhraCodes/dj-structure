from rest_framework.generics import DestroyAPIView
from apps.books.models import Book
from rest_framework.permissions import IsAdminUser

class BookDeleteAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = (IsAdminUser,)