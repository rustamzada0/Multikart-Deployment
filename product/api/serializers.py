from rest_framework import serializers
from ..models import Variant, Product, Category, Vendor, Image, Option


class GetCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
             "id",
             "title_en",
             "parent",
             "slug"
        )
    

class GetProductSerializer(serializers.ModelSerializer):
    variant = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "price",
            "title_en",
            "desc_en",
            "video",
            "slug",
            "variant",
            "category",
            "vendor"
        )

    def get_variant(self, obj):
        serializer = GetOffProductVariantSerializer(obj.related_variants.all(), many=True)
        return serializer.data


class GetOffProductVariantSerializer(serializers.ModelSerializer):
    get_absolute_url = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()

    class Meta:
        model = Variant
        fields = (
            "id",
            "title",
            "actual_price",
            "slug",
            "color",
            "get_absolute_url"
        )
        
    def get_get_absolute_url(self, obj):
        return obj.get_absolute_url()
    
    def get_color(self, obj):
        return obj.color.title


class GetOffVariantProductSerializer(serializers.ModelSerializer):
    category = GetCategorySerializer()
    vendor = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "price",
            "title_en",
            "desc_en",
            "video",
            "slug",
            "category",
            "vendor"
        )
        
    def get_vendor(self, obj):
        return obj.vendor.name


class GetOptionSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()

    class Meta:
        model = Option
        fields = (
            "stock",
            "size"
        )

    def get_size(self, obj):
        return obj.size.title


class GetVariantSerializer(serializers.ModelSerializer):
    product = GetOffVariantProductSerializer()
    get_absolute_url = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    option = serializers.SerializerMethodField()

    class Meta:
        model = Variant
        fields = (
            "id",
            "title",
            "actual_price",
            "slug",
            "color",
            "product",
            "is_main_variant",
            "is_main_image",
            "get_absolute_url",
            "option"
        )
        
    def get_get_absolute_url(self, obj):
        return obj.get_absolute_url()
    
    def get_color(self, obj):
        return obj.color.title
    
    def get_option(self, obj):
        serializer = GetOptionSerializer(obj.related_option.all(), context=self.context, many=True)
        return serializer.data


class GetImageSerializer(serializers.ModelSerializer):
    variant = GetVariantSerializer()

    class Meta:
            model = Image
            fields = (
                "id",
                "image",
                "variant",
            )