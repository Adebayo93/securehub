
from django.contrib import admin

from .models import SecurityService, ServiceArea, ServiceCategory


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(SecurityService)
class SecurityServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company",
        "category",
        "personnel_count",
        "minimum_price",
        "maximum_price",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "name",
        "company__company_name",
        "category__name",
    )


@admin.register(ServiceArea)
class ServiceAreaAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "state",
        "city",
        "address_or_area",
    )

    list_filter = (
        "state",
        "city",
    )

    search_fields = (
        "company__company_name",
        "state",
        "city",
        "address_or_area",
    )

