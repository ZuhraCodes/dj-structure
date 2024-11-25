from rest_framework import serializers
from apps.books.models import Book, BookReview
from apps.sales.models import OrderItem
from django.db.models import Sum

class BookReviewModelSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.first_name")
    
    class Meta:
        model = BookReview
        fields = ("rate", )

class BookListModelSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.full_name")
    sold = serializers.SerializerMethodField()
    book_reviews = BookReviewModelSerializer(source="reviews", many=True)
    
    class Meta:
        model = Book
        fields = ("id", "title", "cover", "price", "author", "sold", "book_reviews",)
        
    def get_sold(self, obj):
        return obj.sold