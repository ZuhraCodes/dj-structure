from django.urls import path
from apps.sales import api_endpoints

urlpatterns = [
    path("add/", api_endpoints.AddCartItemAPIView.as_view(), name="cart-add"),
    path("items/", api_endpoints.CartItemListAPIView.as_view(), name="cart-list"),
    path("delete/", api_endpoints.CartItemDeleteAPIView.as_view(), name="cart-delete"),
    path("order/", api_endpoints.MakeOrderAPIView.as_view(), name="make-order")
]