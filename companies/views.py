from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SecurityCompanyForm
from .models import SecurityCompany


@login_required
def create_company(request):
    if request.user.role != "AGENCY":
        return redirect("dashboard")

    if hasattr(request.user, "security_company"):
        return redirect("companies:company_profile")

    if request.method == "POST":
        form = SecurityCompanyForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.verification_status = (
                SecurityCompany.VerificationStatus.PENDING
            )
            company.save()

            messages.success(
                request,
                "Your company profile has been submitted for admin approval.",
            )

            return redirect("companies:company_profile")
    else:
        form = SecurityCompanyForm()

    return render(
        request,
        "companies/create_company.html",
        {"form": form},
    )


@login_required
def company_profile(request):
    if request.user.role != "AGENCY":
        return redirect("dashboard")

    company = get_object_or_404(
        SecurityCompany,
        owner=request.user,
    )

    return render(
        request,
        "companies/company_profile.html",
        {"company": company},
    )


@login_required
def edit_company(request):
    if request.user.role != "AGENCY":
        return redirect("dashboard")

    company = get_object_or_404(
        SecurityCompany,
        owner=request.user,
    )

    if request.method == "POST":
        form = SecurityCompanyForm(
            request.POST,
            request.FILES,
            instance=company,
        )

        if form.is_valid():
            company = form.save(commit=False)

            company.verification_status = (
                SecurityCompany.VerificationStatus.PENDING
            )

            company.save()

            messages.success(
                request,
                "Your company profile has been updated and sent for review.",
            )

            return redirect("companies:company_profile")
    else:
        form = SecurityCompanyForm(
            instance=company
        )

    return render(
        request,
        "companies/edit_company.html",
        {"form": form},
    )
def company_list(request):
    companies = SecurityCompany.objects.all()

    return render(
        request,
        "companies/company_list.html",
        {"companies": companies},
    )
