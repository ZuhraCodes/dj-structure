from apps.users import api_endpoints
from django.urls import path

urlpatterns = [
    path('login/', api_endpoints.UserLoginAPIView.as_view(), name="login-user")
]