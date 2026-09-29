from django.urls import path

from . import views


app_name = "bookings"


urlpatterns = [
    path(
        "",
        views.booking_list,
        name="booking_list",
    ),

    path(
        "create/",
        views.create_booking,
        name="create_booking",
    ),

    path(
        "<int:booking_id>/",
        views.booking_details,
        name="booking_details",
    ),

    path(
        "agency/",
        views.agency_booking_list,
        name="agency_booking_list",
    ),

    path(
        "agency/update/<int:booking_id>/",
        views.update_booking_status,
        name="update_booking_status",
    ),
]