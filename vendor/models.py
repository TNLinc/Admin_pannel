import uuid

from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Vendor(models.Model):
    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4)
    name = models.TextField(_("name"), null=False, blank=False)
    url = models.URLField(_("url"), null=True, blank=True)

    class Meta:
        managed = False
        verbose_name = _("vendor")
        verbose_name_plural = _("vendors")
        db_table = '"vendor"."vendor"'

    def __str__(self):
        return self.name


class ProductType(models.TextChoices):
    TONAL_CREAM = "TONAL_CREAM", _("TONAL_CREAM")


class VendorColor(models.Model):
    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4)
    name = models.TextField(_("name"), null=False, blank=False)
    color = ColorField(_("color"), null=False, blank=False)
    vendor = models.ForeignKey(
        verbose_name=_("vendor"),
        to="Vendor",
        on_delete=models.CASCADE,
        related_name="colors",
    )

    class Meta:
        managed = False
        verbose_name = _("vendor color")
        verbose_name_plural = _("vendor colors")
        db_table = '"vendor"."vendor_color"'

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4)
    name = models.TextField(_("name"), null=False, blank=False)
    type = models.TextField(
        _("type"), choices=ProductType.choices, null=False, blank=False
    )
    color = models.ForeignKey(
        verbose_name=_("color"),
        to="VendorColor",
        on_delete=models.CASCADE,
        related_name="products",
    )
    vendor = models.ForeignKey(
        verbose_name=_("vendor"),
        to="Vendor",
        on_delete=models.CASCADE,
        related_name="products",
    )
    url = models.TextField(_("url"))

    class Meta:
        managed = False
        verbose_name = _("product")
        verbose_name_plural = _("products")
        db_table = '"vendor"."product"'

    def __str__(self):
        return self.name
