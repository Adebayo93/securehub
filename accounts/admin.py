from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('SecureHub Information', {
            'fields': ('role', 'phone'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('SecureHub Information', {
            'fields': ('role', 'phone'),
        }),
    )

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'is_active',
    )

    list_filter = (
        'role',
        'is_active',
        'is_staff',
    )