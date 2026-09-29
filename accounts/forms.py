from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    phone = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Role.CUSTOMER

        if commit:
            user.save()

        return user


class AgencyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label="Contact First Name",
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label="Contact Last Name",
    )
    phone = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Role.AGENCY

        if commit:
            user.save()

        return user