from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.http import JsonResponse
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from ..models import Product, Image, Category, Variant
from .serializers import GetImageSerializer, GetProductSerializer, GetVariantSerializer
from account.models import WishList


class GenericViewSerializerMixin:
    def get_serializer_class(self):
            return self.serializers_classes[self.request.method]


class ProductDetailApiView(GenericViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializers_classes = {
        "GET": GetProductSerializer,
    }


class VariantDetailApiView(GenericViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Variant.objects.all()
    serializers_classes = {
        "GET": GetVariantSerializer,
    }


class FilterApiView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        category = request.query_params.get('category')
        color = request.query_params.getlist('color')
        # size = request.query_params.getlist('size')
        size = request.query_params.get('size')
        price_min = request.query_params.get('price_min')
        price_max = request.query_params.get('price_max')
        brand = request.query_params.getlist('brand')

        filters = Q()

        if color:
            filters &= Q(variant__color__title__in = color)
        if price_min:
            filters &= Q(variant__actual_price__gte = price_min)
        if price_max:
            filters &= Q(variant__actual_price__lte = price_max)
        if brand:
            filters &= Q(variant__product__vendor__name__in = brand)

        queryset = Image.objects.filter(filters).filter(is_main=True)

        if category:
            cat = Category.objects.filter(slug=category).first()
            if cat.parent:
                queryset = queryset.filter(variant__product__category__slug = category)
            else:
                queryset1 = queryset.filter(variant__product__category__parent = cat)

                child_categories = []
                items_list = []
                queryset2 = []
                cats = Category.objects.all()

                for c in cats:
                    if c.parent:
                        if cat.title == c.title:
                            child_categories.append(c)

                for c in child_categories:
                    items_list.append(queryset.filter(variant__product__category = c))
                
                for item_list in items_list:
                    for item in item_list:
                        queryset2.append(item)

                queryset = list(queryset1) + queryset2

        arr = []
        if size:
            for item in queryset:
                for option in item.variant.related_option.all():
                    if option.size.title == size:
                        arr.append(option.variant)

            arr2 = []
            for i in arr:
                arr2.append(Image.objects.filter(variant=i).filter(is_main=True))

            queryset = []
            for i in arr2:
                for j in i:
                    queryset.append(j)

        serializer = GetImageSerializer(queryset, context={"request": self.request}, many=True)

        return JsonResponse(serializer.data, safe=False)
    

class AddToWishlist(APIView):
    def post(self, request, *args, **kwargs):
        user_id = int(self.request.query_params.get('user_id'))
        variant_id = int(self.request.query_params.get('variant_id'))

        if WishList.objects.filter(user_id=user_id, variant_id=variant_id).exists():

            return Response({"detail": f"This item is already in the wishlist"})
        else:
            WishList.objects.create(user_id=user_id, variant_id=variant_id)

            return Response({"detail": f"Wishlist item with id successfully added"})