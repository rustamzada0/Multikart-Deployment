from rest_framework import serializers
from ..models import Variant, Product, Category, Vendor, Image, Option






# class GetCategorySerializer(serializers.ModelSerializer):
    # product = serializers.SerializerMethodField()
    # child = serializers.SerializerMethodField()

    # class Meta:
    #     model = Category
    #     fields = '__all__'

    # def get_product(self, obj):
    #     serializer = GetCategoryProductSerializer(obj.related_product.all(), context=self.context, many=True)
    #     return serializer.data
    
    # def get_child(self, obj):
    #     serializer = GetCategorySerializer(obj.child.all(), many=True)
    #     return serializer.data


# class GetImageSerializer(serializers.ModelSerializer):
#     class Meta:
#             model = Image
#             fields = '__all__'



# class GetProductCategorySerializer(serializers.ModelSerializer):
#     child = serializers.SerializerMethodField()

#     class Meta:
#         model = Category
#         fields = (
#             "id",
#             "title_en",
#             "title_az",
#             "parent",
#             "slug",
#             "child"
#         )
    
#     def get_child(self, obj):
#         serializer = GetCategorySerializer(obj.child.all(), many=True)
#         return serializer.data


# class GetVendorSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Vendor
#         fields = (
#             "id",
#             "name",
#             "image",
#             "desc",
#             "rating"
#         )


# class GetCategoryProductSerializer(serializers.ModelSerializer):
#     vendor = GetVendorSerializer()
#     variant = serializers.SerializerMethodField()

#     class Meta:
#         model = Product
#         fields = (
#             "id",
#             "title_en",
#             "title_az",
#             "desc_en",
#             "desc_az",
#             "video",
#             "slug",
#             "vendor",
#             "variant"
#         )

#     def get_variant(self, obj):
#         serializer = GetProductVariantSerializer(obj.related_variant.all(), context=self.context, many=True)
#         return serializer.data


# class GetProductSerializer(serializers.ModelSerializer):
#     category = GetProductCategorySerializer()
#     vendor = GetVendorSerializer()
#     variant = serializers.SerializerMethodField()

#     class Meta:
#         model = Product
#         fields = (
#             "id",
#             "title_en",
#             "title_az",
#             "desc_en",
#             "desc_az",
#             "video",
#             "slug",
#             "category",
#             "vendor",
#             "variant"
#         )

#     def get_variant(self, obj):
#         serializer = GetProductVariantSerializer(obj.related_variant.all(), context=self.context, many=True)
#         return serializer.data


# class GetVariantProductSerializer(serializers.ModelSerializer):
#     category = GetProductCategorySerializer()
#     vendor = GetVendorSerializer()

#     class Meta:
#         model = Product
#         fields = (
#             "id",
#             "title_en",
#             "title_az",
#             "desc_en",
#             "desc_az",
#             "video",
#             "slug",
#             "category",
#             "vendor",
#         )


# class GetVariantSerializer(serializers.ModelSerializer):
#     product = GetVariantProductSerializer()
#     image = serializers.SerializerMethodField()
#     option = serializers.SerializerMethodField()

#     class Meta:
#         model = Variant
#         fields = (
#             "id",
#             "title_en",
#             "title_az",
#             "price",
#             "discount_type",
#             "discount_amount",
#             "actual_price",
#             "discount_time",
#             "general_stock",
#             "new_status",
#             "slug",
#             "product",
#             "image",
#             "option"
#         )

#     def get_image(self, obj):
#         serializer = GetImageVariantSerializer(obj.related_image.all(), context=self.context, many=True)
#         return serializer.data
    
#     def get_option(self, obj):
#         serializer = GetOptionVariantSerializer(obj.related_option.all(), context=self.context, many=True)
#         return serializer.data
    

# class GetProductVariantSerializer(serializers.ModelSerializer):
#     image = serializers.SerializerMethodField()
#     option = serializers.SerializerMethodField()

#     class Meta:
#         model = Variant
#         fields = (
#             "id",
#             "title_en",
#             "title_az",
#             "price",
#             "discount_type",
#             "discount_amount",
#             "actual_price",
#             "discount_time",
#             "general_stock",
#             "new_status",
#             "slug",
#             "image",
#             "option"
#         )

#     def get_image(self, obj):
#         serializer = GetImageVariantSerializer(obj.related_image.all(), context=self.context, many=True)
#         return serializer.data
    
#     def get_option(self, obj):
#         serializer = GetOptionVariantSerializer(obj.related_option.all(), context=self.context, many=True)
#         return serializer.data


# class GetImageVariantSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Image
#         fields = (
#             "id",
#             "image",
#             "is_main",
#         )


# class GetVariantImageSerializer(serializers.ModelSerializer):
#     product = GetVariantProductSerializer()
#     option = serializers.SerializerMethodField()

#     class Meta:
#         model = Variant
#         fields = (
#             "id",
#             "title_en",
#             "title_az",
#             "price",
#             "discount_type",
#             "discount_amount",
#             "actual_price",
#             "discount_time",
#             "general_stock",
#             "new_status",
#             "slug",
#             "product",
#             "option"
#         )

#     def get_option(self, obj):
#         serializer = GetOptionVariantSerializer(obj.related_option.all(), context=self.context, many=True)
#         return serializer.data


# class GetImageSerializer(serializers.ModelSerializer):
#     variant = GetVariantImageSerializer()

#     class Meta:
#         model = Image
#         fields = (
#             "id",
#             "image",
#             "is_main",
#             "variant"
#         )


# class GetVariantOptionSerializer(serializers.ModelSerializer):
#     product = GetVariantProductSerializer()
#     image = serializers.SerializerMethodField()

#     class Meta:
#         model = Variant
#         fields = (
#             "id",
#             "title_en",
#             "title_az",
#             "price",
#             "discount_type",
#             "discount_amount",
#             "actual_price",
#             "discount_time",
#             "general_stock",
#             "new_status",
#             "slug",
#             "product",
#             "image",
#         )
        
#     def get_image(self, obj):
#         serializer = GetImageVariantSerializer(obj.related_image.all(), context=self.context, many=True)
#         return serializer.data


# class GetOptionSerializer(serializers.ModelSerializer):
#     variant = GetVariantOptionSerializer()
#     properties = serializers.SerializerMethodField()

#     class Meta:
#         model = Option
#         fields = (
#             "id",
#             "stock",
#             "properties",
#             "variant",
#         )
    
#     def get_properties(self, obj):
#         properties_values = obj.properties.values_list('values', flat=True)
#         return properties_values


# class GetOptionVariantSerializer(serializers.ModelSerializer):
#     properties = serializers.SerializerMethodField()

#     class Meta:
#         model = Option
#         fields = (
#             "id",
#             "stock",
#             "properties",
#         )
    
#     def get_properties(self, obj):
#         properties_values = obj.properties.values_list('values', flat=True)
#         return properties_values


# class PostImageSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Image
#         fields = (
#             "image",
#             "is_main",
#             "variant"
#         )


# class PostVariantSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Variant
#         fields = (
#             "title_en",
#             "title_az",
#             "product",
#             "price",
#             "discount_type",
#             "discount_amount",
#             "actual_price",
#             "discount_time",
#             "general_stock",
#             "new_status",
#         )


# class PostProductSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Product
#         fields = (
#             "title_en",
#             "title_az",
#             "product_detail_en",
#             "product_detail_az",
#             "desc_en",
#             "desc_az",
#             "video",
#             "category",
#             "vendor",
#         )


# class PostOptionSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Option
#         fields = (
#             "stock",
#             "properties",
#             "variant",
#         )