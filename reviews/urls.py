from django.urls import path

from . import views


app_name = "reviews"


urlpatterns = [
    path(
        "",
        views.my_reviews,
        name="my_reviews",
    ),

    path(
        "create/<int:booking_id>/",
        views.create_review,
        name="create_review",
    ),
    path(
    "create/<int:booking_id>/",
    views.create_review,
    name="create_review",
    ),
]