from django.contrib import admin

from vendor.models import Product, Vendor, VendorColor


class ProductInLine(admin.StackedInline):
    model = Product
    extra = 0


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    search_fields = ("id", "name")
    inlines = [ProductInLine]


@admin.register(VendorColor)
class VendorColorAdmin(admin.ModelAdmin):
    list_display = ("name", "color")
    search_fields = ("id", "name", "color")
    inlines = [ProductInLine]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "color")
    search_fields = ("id", "type", "name", "color")
