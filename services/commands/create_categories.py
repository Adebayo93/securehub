from django.core.management.base import BaseCommand

from services.models import ServiceCategory


class Command(BaseCommand):
    help = "Create default SecureHub service categories"

    categories = [
        (
            "Event Security",
            "Security services for weddings, parties, concerts, "
            "conferences, festivals and other events.",
        ),
        (
            "Private Security",
            "Security for homes, estates, families and private properties.",
        ),
        (
            "Corporate Security",
            "Security services for offices, companies, schools, "
            "hotels and institutions.",
        ),
        (
            "Personal Protection",
            "Personal protection services for individuals and clients.",
        ),
        (
            "Escort Services",
            "Security escort and movement protection services.",
        ),
    ]

    def handle(self, *args, **options):
        for name, description in self.categories:
            category, created = ServiceCategory.objects.get_or_create(
                name=name,
                defaults={
                    "description": description,
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created category: {category.name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Category already exists: {category.name}"
                    )
                )