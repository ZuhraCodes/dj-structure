from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.utils import timezone

class User(AbstractUser):
    class UserRole(models.TextChoices):
        USER = "user", _("User")
        SALESMAN  = "salesman", _("Salesman")
        
    role = models.CharField(_("Role"), choices=UserRole.choices, max_length=16)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
class OneTimeCode(models.Model):
    code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_expired(self):
        return (timezone.now() - self.created_at).seconds > 60