from django import forms

from .models import SecurityCompany


class SecurityCompanyForm(forms.ModelForm):
    class Meta:
        model = SecurityCompany
        fields = (
            "company_name",
            "logo",
            "description",
            "email",
            "phone",
            "address",
            "city",
            "state",
            "website",
            "years_of_experience",
        )

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe your security company...",
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),
        }