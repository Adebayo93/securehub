from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review

        fields = [
            "rating",
            "comment",
        ]

        widgets = {
            "rating": forms.Select(
                choices=[
                    (5, "5 - Excellent"),
                    (4, "4 - Very Good"),
                    (3, "3 - Good"),
                    (2, "2 - Fair"),
                    (1, "1 - Poor"),
                ],
                attrs={
                    "class": "form-control",
                },
            ),

            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Tell us about your experience...",
                }
            ),
        }