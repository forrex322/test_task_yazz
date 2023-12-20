from django.db.models.signals import post_save
from django.dispatch import receiver

from shops.models import Product


@receiver(post_save, sender=Product)
def check_categories(sender, instance=None, created=False, **kwargs):
    if created:
        product_categories = instance.categories.all()
        allowed_shop_categories = instance.shop.allowed_categories.all()

        for category in product_categories:
            if category not in allowed_shop_categories:
                raise ValueError(
                    f"This product contains categories not allowed for store {instance.shop.name}"
                )
