from django.db import models

# Create your models here.

class Extra(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    old_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    badge_text = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    active = models.BooleanField(default=True)
    extras = models.ManyToManyField(Extra, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductPortion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='portions')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    order = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'price']

    def __str__(self):
        return f"{self.product.name} - {self.name} (${self.price})"

