from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from companies.models import SecurityCompany

from .forms import SecurityServiceForm
from .models import ServiceCategory, SecurityService


@login_required
def service_list(request):
    """
    Customer marketplace.
    Only active services from approved agencies are shown.
    """

    services = (
        SecurityService.objects.filter(
            is_active=True,
            company__verification_status=(
                SecurityCompany.VerificationStatus.APPROVED
            ),
        )
        .select_related("company", "category")
    )

    search = request.GET.get("search", "").strip()
    category = request.GET.get("category", "").strip()
    state = request.GET.get("state", "").strip()
    city = request.GET.get("city", "").strip()
    minimum_price = request.GET.get("minimum_price", "").strip()
    maximum_price = request.GET.get("maximum_price", "").strip()

    if search:
        services = services.filter(
            Q(name__icontains=search)
            | Q(company__company_name__icontains=search)
            | Q(description__icontains=search)
        )

    if category:
        services = services.filter(category_id=category)

    if state:
        services = services.filter(
            company__state__iexact=state
        )

    if city:
        services = services.filter(
            company__city__icontains=city
        )

    if minimum_price:
        try:
            services = services.filter(
                minimum_price__gte=float(minimum_price)
            )
        except ValueError:
            pass

    if maximum_price:
        try:
            services = services.filter(
                maximum_price__lte=float(maximum_price)
            )
        except ValueError:
            pass

    categories = ServiceCategory.objects.all().order_by("name")

    states = (
        SecurityCompany.objects.filter(
            verification_status=(
                SecurityCompany.VerificationStatus.APPROVED
            )
        )
        .values_list("state", flat=True)
        .distinct()
        .order_by("state")
    )

    return render(
        request,
        "services/service_list.html",
        {
            "services": services,
            "categories": categories,
            "states": states,
            "search": search,
            "selected_category": category,
            "selected_state": state,
            "city": city,
            "minimum_price": minimum_price,
            "maximum_price": maximum_price,
        },
    )


@login_required
def service_details(request, service_id):
    """
    Show details of an approved security service.
    """

    service = get_object_or_404(
        SecurityService.objects.select_related(
            "company",
            "category",
        ),
        id=service_id,
        is_active=True,
        company__verification_status=(
            SecurityCompany.VerificationStatus.APPROVED
        ),
    )

    return render(
        request,
        "services/service_details.html",
        {
            "service": service,
        },
    )


@login_required
def my_services(request):
    """
    Show services belonging to the logged-in agency.
    """

    if request.user.role != "AGENCY":
        return redirect("dashboard")

    company = get_object_or_404(
        SecurityCompany,
        owner=request.user,
    )

    services = (
        SecurityService.objects.filter(
            company=company
        )
        .select_related(
            "company",
            "category",
        )
    )

    return render(
        request,
        "services/my_services.html",
        {
            "services": services,
        },
    )


@login_required
def add_service(request):
    """
    Allow an approved agency to add a new security service.
    """

    if request.user.role != "AGENCY":
        return redirect("dashboard")

    company = get_object_or_404(
        SecurityCompany,
        owner=request.user,
    )

    if company.verification_status != (
        SecurityCompany.VerificationStatus.APPROVED
    ):
        return redirect("agency_dashboard")

    if request.method == "POST":
        form = SecurityServiceForm(request.POST)

        if form.is_valid():
            service = form.save(commit=False)
            service.company = company
            service.save()

            return redirect("services:my_services")

    else:
        form = SecurityServiceForm()

    return render(
        request,
        "services/add_service.html",
        {
            "form": form,
        },
    )