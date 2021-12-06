from django.core.management.base import BaseCommand
from django.db import transaction

from vendor.factories import ProductFactory, VendorColorFactory, VendorFactory
from vendor.models import Product, Vendor, VendorColor

NUM_VENDOR = 10
NUM_VENDOR_COLOR = 20
NUM_PRODUCT = 100


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [
            Vendor,
            VendorColor,
            Product,
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_VENDOR):
            VendorFactory()

        for _ in range(NUM_VENDOR_COLOR):
            VendorColorFactory()

        for _ in range(NUM_PRODUCT):
            ProductFactory()
