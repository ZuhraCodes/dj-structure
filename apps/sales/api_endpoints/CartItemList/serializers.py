from rest_framework import serializers
from apps.books.models import Book, Author
from apps.users.models import CartItem

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("full_name",)

class CartItemDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ("title", "description", "cover", "price", "author")

class CartItemListSerializer(serializers.ModelSerializer):
    book = CartItemDetailSerializer()
    class Meta:
        model = CartItem
        fields = ("book", "quantity")