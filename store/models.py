from django.db import models
from django.contrib.auth.models import AbstractUser
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
