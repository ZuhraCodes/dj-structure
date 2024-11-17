from rest_framework.generics import ListAPIView
from apps.users.models import CartItem
from rest_framework import permissions
from apps.sales.models import Order, OrderItem
from rest_framework.response import Response


class MakeOrderAPIView(ListAPIView):
    queryset = CartItem.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    
    def post(self, request, *args, **kwargs):
        cart_items = request.user.cart_items.all()
        order = Order.objects.create(user=request.user)
        order_items = []
        
        for cart_item in cart_items:
            order_items.append(
                OrderItem(
                    order=order,
                    book=cart_item.book,
                    price=cart_item.book.price,
                    quantity=cart_item.quantity
                )
            )
        OrderItem.objects.bulk_create(order_items) 
        cart_items.delete()
        return Response({"message": "Order created successfully"})
        
__all__ = ['MakeOrderAPIView']