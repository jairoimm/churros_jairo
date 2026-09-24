from django.db import models

# Create your models here.

from django.db import models


class Order(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pendiente"),
        ("paid", "Pagado"),
        ("preparing", "Preparando"),
        ("delivering", "En Reparto"),
        ("delivered", "Entregado"),
        ("cancelled", "Cancelado"),
    ]

    DELIVERY_CHOICES = [
        ("pickup", "Retiro"),
        ("delivery", "Delivery"),
    ]

    customer_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    delivery_type = models.CharField(max_length=20,choices=DELIVERY_CHOICES)
    total = models.DecimalField(max_digits=10,decimal_places=0)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id}"

class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product_name = models.CharField(
        max_length=200
    )

    quantity = models.IntegerField()

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    def __str__(self):
        return self.product_name