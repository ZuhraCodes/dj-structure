from rest_framework import serializers
from apps.books.models import Book

class BookUpdateModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Book
        fields = ("id", "title", "description", "cover", "price", "author", "quantity")