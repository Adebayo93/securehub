from django.urls import path

from .views import (
    company_profile,
    create_company,
    edit_company,
    company_list,
)

app_name = "companies"

urlpatterns = [
    path(
        "",
        company_list,
        name="company_list",
    ),

    path(
        "create/",
        create_company,
        name="create_company",
    ),

    path(
        "profile/",
        company_profile,
        name="company_profile",
    ),

    path(
        "edit/",
        edit_company,
        name="edit_company",
    ),
]