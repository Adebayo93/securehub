from django.db import models

from companies.models import SecurityCompany


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SecurityService(models.Model):
    company = models.ForeignKey(
        SecurityCompany,
        on_delete=models.CASCADE,
        related_name="services",
    )

    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.PROTECT,
        related_name="services",
    )

    name = models.CharField(max_length=200)
    description = models.TextField()

    minimum_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    maximum_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    personnel_count = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.company.company_name} - {self.name}"


class ServiceArea(models.Model):
    company = models.ForeignKey(
        SecurityCompany,
        on_delete=models.CASCADE,
        related_name="service_areas",
    )

    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    address_or_area = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["state", "city"]

    def __str__(self):
        location = self.state

        if self.city:
            location = f"{self.city}, {location}"

        return f"{self.company.company_name} - {location}"