from rest_framework import serializers
from .models import Cart, CartItems
from products.models import ProductVariation
from products.serializers import ProductSerializer
from accounts.serializers import ProfileSerializer


class CartSerializer(serializers.ModelSerializer):
    owner_username = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ("user", "owner_username")

    def get_owner_username(self, obj):
        user = obj.user
        user_serializer = ProfileSerializer(instance=user)
        return user_serializer.data["username"]


class CartItemsSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    product_variation_details = serializers.SerializerMethodField()

    class Meta:
        model = CartItems
        fields = (
            "product",
            "product_name",
            "product_variation_details",
            "quantity",
            "total_price",
        )

    def get_product_name(self, obj):
        product = obj.product
        serializer_product = ProductSerializer(instance=product)
        return serializer_product.data["title"]

    def get_product_variation_details(self, obj):
        product_variation = obj.product_variation
        return {
            "variation_id": product_variation.id,
            "size": product_variation.size,
        }


class SessionCartSerializer(serializers.Serializer):
    def to_representation(self, instance):
        items = []
        for item in instance:
            item_data = item.copy()
            product = item_data.pop("product")
            variation = item_data.get("variation")

            item_data["product_title"] = product.title
            item_data["product_id"] = product.id
            item_data["product_variation"] = {
                "variation_id": variation.id,
                "size": variation.size,
            }
            item_data["total_price"] = (
                item_data.get("price_with_discount", item_data["price"])
                * item_data["quantity"]
            )
            items.append(item_data)

        return {"items": items}