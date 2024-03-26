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

    # ? `upload_to` here refers to a firectory inside the project `ecommerce`
    # ? but outside of app `store`
    image = models.ImageField(upload_to="files/images")

    def __str__(self) -> str:
        return f"""Name: {self.name}
    Price: {self.price}
    Image: {self.image}
    """
