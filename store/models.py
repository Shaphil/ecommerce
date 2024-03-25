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

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        return super().save(*args, **kwargs)
