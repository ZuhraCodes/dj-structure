from rest_framework.generics import ListAPIView
from .serializers import CartItemListSerializer
from apps.users.models import CartItem
from rest_framework import permissions

class CartItemListAPIView(ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)