from django.urls import path

from . import views


app_name = "services"


urlpatterns = [
    path(
        "",
        views.service_list,
        name="service_list",
    ),
    path(
        "add/",
        views.add_service,
        name="add_service",
    ),
    path(
        "my-services/",
        views.my_services,
        name="my_services",
    ),
    path(
        "<int:service_id>/",
        views.service_details,
        name="service_details",
    ),
]