from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class UserType(models.TextChoices):
        BUYER = "BUYER", _("Buyer")
        SELLER = "SELLER", _("Seller")

    role = models.CharField(
        max_length=8,
        choices=UserType,
        default=UserType.SELLER
    )


class Product(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    # ? `upload_to` here refers to a directory inside the project `ecommerce`
    # ? but outside of app `store`
    image = models.ImageField(upload_to="files/images")

    def __str__(self) -> str:
        return f"Product: {self.name} - Price: {self.price} - Image: {self.image}"


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name="cart", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.price = self.quantity * self.product.price
        super().save()

    def __str__(self):
        return f"Item: {self.product.name} - Quantity: {self.quantity} - Price: {self.price}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    items = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Cart'

    def __str__(self):
        return f"User: {self.user.username} - Total: {self.total_price}"


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name="cartOrder")
    is_created = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order: {self.cart.user.username}"


class DailyData(models.Model):
    revenue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Daily Data'

    def __str__(self):
        return f"Daily Data: {self.revenue}"
