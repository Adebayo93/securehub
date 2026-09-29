from django import forms

from .models import SecurityService


class SecurityServiceForm(forms.ModelForm):

    class Meta:
        model = SecurityService

        fields = [
            "category",
            "name",
            "description",
            "minimum_price",
            "maximum_price",
            "personnel_count",
            "is_active",
        ]

        widgets = {
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter security service name",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Describe the security service",
                    "rows": 5,
                }
            ),

            "minimum_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Minimum price",
                    "step": "0.01",
                }
            ),

            "maximum_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Maximum price",
                    "step": "0.01",
                }
            ),

            "personnel_count": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Number of security personnel",
                    "min": 1,
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        minimum_price = cleaned_data.get("minimum_price")
        maximum_price = cleaned_data.get("maximum_price")

        if (
            minimum_price is not None
            and maximum_price is not None
            and minimum_price > maximum_price
        ):
            raise forms.ValidationError(
                "Minimum price cannot be greater than maximum price."
            )

        return cleaned_data