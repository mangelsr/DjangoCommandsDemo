from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.orders.models import Order


class Command(BaseCommand):
    help = "Elimina órdenes antiguas con un estado específico"

    def add_arguments(self, parser):
        parser.add_argument(
            "--days",
            type=int,
            default=90,
            help="Número de días hacia atrás para eliminar órdenes",
        )
        parser.add_argument(
            "--status",
            type=str,
            required=True,
            help="Estado de las órdenes a eliminar (e.g., CANCELLED)",
        )

    def handle(self, *args, **options):
        days = options["days"]
        status = options["status"]
        cutoff_date = timezone.now() - timedelta(days=days)

        orders_to_delete = Order.objects.filter(
            status=status, created_at__lte=cutoff_date
        )
        count = orders_to_delete.count()
        orders_to_delete.delete()

        self.stdout.write(
            self.style.SUCCESS(
                f"Se han eliminado {count} órdenes con estado '{status}' anteriores a {days} días."
            )
        )
