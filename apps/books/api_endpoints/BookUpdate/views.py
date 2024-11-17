from rest_framework.generics import UpdateAPIView
from .serializers import BookUpdateModelSerializer
from apps.books.models import Book
from rest_framework.permissions import IsAdminUser

class BookUpdateAPIView(UpdateAPIView):
    http_method_names = ['patch']
    queryset = Book.objects.all()
    serializer_class = BookUpdateModelSerializer
    permission_classes = (IsAdminUser,)