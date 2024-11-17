from rest_framework import serializers
from apps.books.models import Book

class BookListModelSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.full_name")
    
    class Meta:
        model = Book
        fields = ("title", "cover", "price", "author",)