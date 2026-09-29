from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from accounts.views import auth_page



def home(request):
    return render(request, "home.html")


urlpatterns = [
    path("auth/", auth_page, name="auth"),
    path("", home, name="home"),

    path("admin/", admin.site.urls),

    path(
        "accounts/",
        include("accounts.urls"),
    ),

    path(
        "companies/",
        include("companies.urls"),
    ),

    path(
        "services/",
        include("services.urls"),
    ),
    path(
         "bookings/",
         include("bookings.urls"),
    ),
    path(
    "reviews/",
    include("reviews.urls"),
    ),

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )