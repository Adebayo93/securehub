from django.conf import settings
from django.db import models

from bookings.models import Booking
from companies.models import SecurityCompany


class Review(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name="review",
    )

    company = models.ForeignKey(
        SecurityCompany,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    rating = models.PositiveIntegerField()

    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer} - {self.company} - {self.rating}/5"