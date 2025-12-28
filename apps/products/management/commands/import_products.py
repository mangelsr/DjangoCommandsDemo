import csv

from django.core.management.base import BaseCommand

from apps.products.models import Product, Category


class Command(BaseCommand):
    help = "Importa productos desde un archivo CSV, con opción de actualizar productos existentes"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Ruta del archivo CSV")
        parser.add_argument(
            "--update", action="store_true", help="Actualizar productos existentes"
        )

    def handle(self, *args, **options):
        file_path = options["file_path"]
        update = options["update"]

        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0

            for row in reader:
                category, _ = Category.objects.get_or_create(name=row["category"])

                if update:
                    product, created = Product.objects.update_or_create(
                        name=row["name"],
                        defaults={
                            "description": row["description"],
                            "price": float(row["price"]),
                            "stock": int(row["stock"]),
                            "category": category,
                        },
                    )
                else:
                    product = Product(
                        name=row["name"],
                        description=row["description"],
                        price=float(row["price"]),
                        stock=int(row["stock"]),
                        category=category,
                    )
                    product.save()

                count += 1

        self.stdout.write(
            self.style.SUCCESS(f"Se han importado {count} productos desde {file_path}.")
        )
