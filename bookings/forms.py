
from django import forms

from services.models import SecurityService

from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            "service",
            "event_date",
            "event_time",
            "location",
            "number_of_guards",
            "message",
        ]

        widgets = {
            "service": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),

            "event_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "event_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter event location",
                }
            ),

            "number_of_guards": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "placeholder": "Number of security guards",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Additional information",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["service"].queryset = (
            SecurityService.objects.filter(
                is_active=True,
                company__verification_status="APPROVED",
            )
            .select_related(
                "company",
                "category",
            )
            .order_by(
                "company__company_name",
                "name",
            )
        )