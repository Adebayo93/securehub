from django.urls import path

from .views import (
    SecureHubLoginView,
    auth_page,
    agency_dashboard,
    admin_dashboard,
    customer_dashboard,
    dashboard,
    logout_view,
    profile,
    register_agency,
    register_customer,
)



urlpatterns = [
    path(
    "auth/",
    auth_page,
    name="auth",
),
    path(
        "register/customer/",
        register_customer,
        name="register_customer",
    ),

    path(
        "register/agency/",
        register_agency,
        name="register_agency",
    ),

    path(
        "login/",
        SecureHubLoginView.as_view(),
        name="login",
    ),

    path(
        "logout/",
        logout_view,
        name="logout",
    ),

    path(
        "dashboard/",
        dashboard,
        name="dashboard",
    ),

    path(
        "dashboard/customer/",
        customer_dashboard,
        name="customer_dashboard",
    ),

    path(
        "dashboard/agency/",
        agency_dashboard,
        name="agency_dashboard",
    ),

    path(
        "dashboard/admin/",
        admin_dashboard,
        name="admin_dashboard",
    ),

    path(
        "profile/",
        profile,
        name="profile",
    ),
]