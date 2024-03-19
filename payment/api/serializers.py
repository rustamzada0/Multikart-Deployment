from rest_framework import serializers
from product.api.serializers import GetVariantSerializer
from ..models import CartItem

class PostAddToCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem

        fields = (
            'cart',
            'variant',
            'size',
            'quantity',
        )

class GetCartListSerializer(serializers.ModelSerializer):
    variant = GetVariantSerializer()

    class Meta:
        model = CartItem

        fields = (
            'id',
            'variant',
            'quantity',
            'size',
            'total_price',
            'done'
        )