import graphene
from django.db.models import Subquery, OuterRef
from graphene_django import DjangoObjectType
from shops.models import Product, Shop


class ShopType(DjangoObjectType):
    class Meta:
        model = Shop
        field = ("id", "name")


class Query(graphene.ObjectType):
    list_lowest_product_from_each_shop = graphene.List(ShopType)

    def resolve_list_lowest_product_from_each_shop(root, info):
        return (
            Shop.objects.annotate(
                lowest_price_product_id=Subquery(
                    Product.objects.filter(shop=OuterRef("pk"))
                    .order_by("price")
                    .values("id")[:1]
                )
            )
            .prefetch_related("products")
            .values_list("id", "lowest_price_product_id", flat=True)
        )


schema = graphene.Schema(query=Query)
