import factory
from factory.django import DjangoModelFactory

from vendor.models import Product, ProductType, Vendor, VendorColor


class VendorFactory(DjangoModelFactory):
    class Meta:
        model = Vendor

    name = factory.Faker("company")
    url = factory.Faker("url")


class VendorColorFactory(DjangoModelFactory):
    class Meta:
        model = VendorColor

    name = factory.Faker("catch_phrase")
    color = factory.Faker("hex_color")
    vendor = factory.Iterator(Vendor.objects.all())


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("catch_phrase")
    type = ProductType.TONAL_CREAM
    color = factory.Iterator(VendorColor.objects.all())
    vendor = factory.Iterator(Vendor.objects.all())
    url = factory.Faker("url")
