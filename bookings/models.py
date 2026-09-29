
from django.conf import settings
from django.db import models

from services.models import SecurityService


class Booking(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("ACCEPTED", "Accepted"),
        ("REJECTED", "Rejected"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings",
    )

    service = models.ForeignKey(
        SecurityService,
        on_delete=models.CASCADE,
        related_name="bookings",
    )

    event_date = models.DateField()

    event_time = models.TimeField()

    location = models.CharField(max_length=255)

    number_of_guards = models.PositiveIntegerField(default=1)

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.service}"

