from rest_framework.generics import DestroyAPIView
from apps.users.models import CartItem
from rest_framework.permissions import IsAuthenticated

class CartItemDeleteAPIView(DestroyAPIView):
    queryset = CartItem.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)