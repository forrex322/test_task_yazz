from django.core.validators import MaxLengthValidator
from django.db import models
from django.contrib.gis.db import models as gis_models
from model_utils import Choices
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class Shop(TimeStampedModel):
    TYPE_OF_SHOP = Choices(
        ("SPORT", _("Sport")), ("FOOD", _("Food")), ("ELECTRONIC", _("Electronic"))
    )

    name = models.CharField(max_length=150, verbose_name=_("Name of shop"))
    description = models.TextField(
        verbose_name=_("Description of shop"),
        null=True,
        blank=True,
        validators=[MaxLengthValidator(500)],
    )
    type_of_shop = models.CharField(
        verbose_name=_("Shop type"),
        max_length=10,
        choices=TYPE_OF_SHOP,
    )
    coordinates = gis_models.PointField()
    commission_rate = models.DecimalField(
        max_digits=2, decimal_places=2, default=0, verbose_name=_("Sales commission")
    )
    allowed_categories = models.ManyToManyField("shops.Category")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Name of category"))

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(max_length=150, verbose_name=_("Name of product"))
    description = models.TextField(
        verbose_name=_("Description of product"),
        null=True,
        blank=True,
        validators=[MaxLengthValidator(500)],
    )
    shop = models.ForeignKey(
        "shops.Shop",
        verbose_name=_("Shop"),
        related_name="products",
        on_delete=models.CASCADE,
    )
    categories = models.ManyToManyField("shops.Category")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price in uah")
    )
    keywords = models.CharField(max_length=150, verbose_name=_("Keywords for product"))

    def __str__(self):
        return self.name
