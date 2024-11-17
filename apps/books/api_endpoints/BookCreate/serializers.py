from rest_framework import serializers
from apps.books.models import Book

class BookCreateModelSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Book
        fields = (
            "title_uz", "title_ru", "title_en",
            "description_uz", "description_ru", "description_en",
            "cover", 
            "price", 
            "author",
            "quantity"
        )