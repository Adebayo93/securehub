from django.contrib import admin

from .models import SecurityCompany


@admin.register(SecurityCompany)
class SecurityCompanyAdmin(admin.ModelAdmin):

    list_display = (
        "company_name",
        "owner",
        "city",
        "state",
        "verification_status",
        "created_at",
    )

    list_filter = (
        "verification_status",
        "state",
        "city",
    )

    search_fields = (
        "company_name",
        "owner__username",
        "owner__email",
        "city",
        "state",
    )

    list_editable = (
        "verification_status",
    )