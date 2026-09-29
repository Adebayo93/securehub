from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from bookings.models import Booking

from .forms import ReviewForm
from .models import Review


@login_required
def my_reviews(request):
    if request.user.role != "CUSTOMER":
        return redirect("dashboard")

    reviews = (
        Review.objects
        .filter(customer=request.user)
        .select_related("company", "booking", "booking__service")
    )

    return render(
        request,
        "reviews/my_reviews.html",
        {
            "reviews": reviews,
        },
    )


@login_required
def create_review(request, booking_id):
    if request.user.role != "CUSTOMER":
        return redirect("dashboard")

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        customer=request.user,
        status="COMPLETED",
    )

    if hasattr(booking, "review"):
        return redirect("reviews:my_reviews")

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)

            review.customer = request.user
            review.booking = booking
            review.company = booking.service.company

            review.save()

            messages.success(
                request,
                "Your review has been submitted successfully.",
            )

            return redirect("reviews:my_reviews")

    else:
        form = ReviewForm()

    return render(
        request,
        "reviews/create_review.html",
        {
            "form": form,
            "booking": booking,
        },
    )