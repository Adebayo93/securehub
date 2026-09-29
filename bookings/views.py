from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from services.models import SecurityService

from .forms import BookingForm
from .models import Booking


@login_required
def create_booking(request):

    if request.user.role != "CUSTOMER":
        return redirect("dashboard")

    service_id = request.GET.get("service")

    selected_service = None

    if service_id:
        selected_service = get_object_or_404(
            SecurityService,
            id=service_id,
            is_active=True,
            company__verification_status="APPROVED",
        )

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)

            booking.customer = request.user
            booking.status = "PENDING"

            booking.save()

            messages.success(
                request,
                "Your booking request has been submitted successfully.",
            )

            return redirect("bookings:booking_list")

    else:
        form = BookingForm(
            initial={
                "service": selected_service,
            }
        )

    return render(
        request,
        "bookings/create_bookings.html",
        {
            "form": form,
            "selected_service": selected_service,
        },
    )


@login_required
def booking_list(request):

    if request.user.role != "CUSTOMER":
        return redirect("dashboard")

    bookings = (
        Booking.objects
        .filter(customer=request.user)
        .select_related(
            "service",
            "service__company",
        )
    )

    return render(
        request,
        "bookings/booking_list.html",
        {
            "bookings": bookings,
        },
    )


@login_required
def booking_details(request, booking_id):

    if request.user.role != "CUSTOMER":
        return redirect("dashboard")

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        customer=request.user,
    )

    return render(
        request,
        "bookings/booking_details.html",
        {
            "booking": booking,
        },
    )


@login_required
def agency_booking_list(request):

    if request.user.role != "AGENCY":
        return redirect("dashboard")

    bookings = (
        Booking.objects
        .filter(
            service__company__owner=request.user
        )
        .select_related(
            "customer",
            "service",
            "service__company",
        )
    )

    return render(
        request,
        "bookings/booking_list.html",
        {
            "bookings": bookings,
            "agency_view": True,
        },
    )


@login_required
def update_booking_status(request, booking_id):

    if request.user.role != "AGENCY":
        return redirect("dashboard")

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        service__company__owner=request.user,
    )

    if request.method == "POST":

        new_status = request.POST.get("status")

        allowed_statuses = [
            "ACCEPTED",
            "REJECTED",
            "COMPLETED",
            "CANCELLED",
        ]

        if new_status in allowed_statuses:
            booking.status = new_status
            booking.save()

            messages.success(
                request,
                "Booking status updated successfully.",
            )

    return redirect("bookings:booking_list")