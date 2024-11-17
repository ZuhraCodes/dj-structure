from rest_framework import serializers
from apps.books.models import Book
from rest_framework.exceptions import ValidationError
from apps.users.models import CartItem

class AddCartItemSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    qty = serializers.IntegerField()
    
    def create(self, validated_data):
        book_id = validated_data["book_id"]
        quantity = validated_data["qty"]
        user = self.context["request"].user
        try:
            book = Book.objects.get(id=book_id)
            
            if quantity > book.quantity:
                raise ValidationError({"error": "We don't have enough book quantity"})
            
            CartItem.objects.update_or_create(
                book=book,
                user=user,
                defaults={
                    "quantity": quantity
                }
            )
            
            return {"message": "Product added successfully"}
        except Book.DoesNotExist:
            raise ValidationError({"error": "Book not found"})
