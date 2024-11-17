from django.db import models

class Order(models.Model):
    class OrderStatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        DELIVERING = 'delivering', 'Delivering process'
        DELIVERED = 'delivered', 'Order completed'
        
    user = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="orders")
    status = models.CharField(
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.PENDING,
        max_length=16
    )
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    book = models.ForeignKey("books.Book", on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)