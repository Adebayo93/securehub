from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import CustomerRegistrationForm, AgencyRegistrationForm


def auth_page(request):
    return render(
        request,
        "accounts/auth.html",
    )


def register_customer(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Your customer account has been created successfully.",
            )

            return redirect("dashboard")
    else:
        form = CustomerRegistrationForm()

    return render(
        request,
        "accounts/register_customer.html",
        {"form": form},
    )


def register_agency(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = AgencyRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Your agency account has been created successfully.",
            )

            return redirect("companies:create_company")
    else:
        form = AgencyRegistrationForm()

    return render(
        request,
        "accounts/register_agency.html",
        {"form": form},
    )


class SecureHubLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return "/accounts/dashboard/"


@login_required
def logout_view(request):
    logout(request)

    messages.success(
        request,
        "You have been logged out successfully.",
    )

    return redirect("login")


@login_required
def dashboard(request):
    if request.user.role == "AGENCY":
        return redirect("agency_dashboard")

    if request.user.role == "ADMIN":
        return redirect("admin_dashboard")

    return redirect("customer_dashboard")


@login_required
def customer_dashboard(request):
    if request.user.role != "CUSTOMER":
        return redirect("dashboard")

    return render(
        request,
        "accounts/customer_dashboard.html",
    )


@login_required
def agency_dashboard(request):
    if request.user.role != "AGENCY":
        return redirect("dashboard")

    company = getattr(
        request.user,
        "security_company",
        None,
    )

    return render(
        request,
        "accounts/agency_dashboard.html",
        {
            "company": company,
        },
    )


@login_required
def admin_dashboard(request):
    if request.user.role != "ADMIN":
        return redirect("dashboard")

    return render(
        request,
        "accounts/admin_dashboard.html",
    )


@login_required
def profile(request):
    return render(
        request,
        "accounts/profile.html",
    )