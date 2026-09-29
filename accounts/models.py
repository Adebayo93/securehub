from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        AGENCY = "AGENCY", "Security Agency"
        ADMIN = "ADMIN", "Administrator"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"