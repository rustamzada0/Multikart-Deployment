# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.generics import ListAPIView, ListCreateAPIView, 
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

# class VariantListApiView(GenericViewSerializerMixin, ListCreateAPIView):
#     queryset = Variant.objects.all()
#     serializers_classes = {
#         "GET": GetVariantSerializer,
#         "POST": PostVariantSerializer
#     }

#     def list(self, request, *args, **kwargs):
#             qs = self.get_queryset()
#             print(qs)
#             title_en = request.query_params.get('title_en')
#             title_az = request.query_params.get('title_az')
#             category = request.query_params.get('category')
#             if title_en:
#                 qs =  qs.filter(title_en__icontains=title_en)
#             data = self.get_serializer(qs, many=True).data

#             if title_az:
#                 qs =  qs.filter(title_az__icontains=title_az)
#             data = self.get_serializer(qs, many=True).data

#             # if category:
#             #     qs =  qs.filter(product__category=category)
#             #     print(qs)
#             # data = self.get_serializer(qs, many=True).data
#             return Response(data)


# class VariantDetailApiView(GenericViewSerializerMixin, RetrieveUpdateDestroyAPIView):
#     queryset = Variant.objects.all()
#     serializers_classes = {
#         "GET": GetVariantSerializer,
#         # "PATCH": PostVariantSerializer,
#         # "PUT": PostVariantSerializer
#     }


# class ProductListApiView(GenericViewSerializerMixin, ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializers_classes = {
#         "GET": GetProductSerializer,
#         # "POST": PostProductSerializer
#     }
#     permission_classes = [IsAuthenticated]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ["title_en",]


# class OptionListApiView(GenericViewSerializerMixin, ListCreateAPIView):
#     queryset = Option.objects.all()
#     serializers_classes = {
#         "GET": GetOptionSerializer,
#         "POST": PostOptionSerializer
#     }
#     # filterset_fields = ["title_en", "title_az"]


# class ImageListApiView(GenericViewSerializerMixin, ListCreateAPIView):
#     queryset = Image.objects.all()
#     serializers_classes = {
#          "GET": GetImageSerializer,
#          "POST": PostImageSerializer
#     }

# context={"request": self.request}

# class CategoryApiView(APIView):
#     def get(self, *args, **kwargs):
#         category = self.request.query_params.get('category')
#         color = self.request.query_params.get('color')

#         filters = Q()
#         if category:
#             filters &= Q(id=category)
#         queryset = Category.objects.filter(filters)
#         print(queryset)
            # qs =  qs.filter(id=category)
            # print(qs)
            # if qs[0].parent:
            #     items = Image.objects.filter(variant__product__category = qs[0]).filter(variant__is_main_variant=True).filter(is_main=True)
            #     print(items)
            # else:
            #     child_categories1 = []
            #     cats = Category.objects.all()
            #     for cat in cats:
            #         if cat.parent:
            #             if qs[0].title == cat.title:
            #                 child_categories1.append(cat)
            #     child_categories2 = Category.objects.filter(parent=qs[0])

            #     items_list = []
            #     items = []

            #     for cat in child_categories1:
            #         items_list.append(Image.objects.filter(variant__product__category = cat).filter(variant__is_main_variant=True).filter(is_main=True))
            #     for cat in child_categories2:
            #         items_list.append(Image.objects.filter(variant__product__category = cat).filter(variant__is_main_variant=True).filter(is_main=True))
            #     for item_list in items_list:
            #         for item in item_list:
            #             items.append(item)

        # print(items)
        # categories = Category.objects.all()
        # serializer = GetCategorySerializer(categories,  many=True)


# class CategoryApiView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = GetImageSerializer

#     def list(self, request, *args, **kwargs):
#         qs = self.get_queryset()
#         items = Image.objects.filter(is_main=True).filter(variant__is_main_variant=True)

#         category = request.query_params.get('category')
#         color = request.query_params.get('color')

#         if category and color:
#             qs =  qs.filter(id=category)
#             if qs[0].parent:
#                 items = Image.objects.filter(variant__product__category = qs[0]).filter(is_main=True).filter(variant__color__title__icontains=color)
#             else:
#                 child_categories1 = []
#                 cats = Category.objects.all()
#                 for cat in cats:
#                     if cat.parent:
#                         if qs[0].title == cat.title:
#                             child_categories1.append(cat)
#                 child_categories2 = Category.objects.filter(parent=qs[0])

#                 items_list = []
#                 items = []
#                 for cat in child_categories1:
#                     items_list.append(Image.objects.filter(variant__product__category = cat).filter(variant__color__title__icontains=color).filter(is_main=True))
#                 for cat in child_categories2:
#                     items_list.append(Image.objects.filter(variant__product__category = cat).filter(variant__color__title__icontains=color).filter(is_main=True))

#                 for item_list in items_list:
#                     for item in item_list:
#                         items.append(item)

#         elif category is not None and color is None:
#             qs =  qs.filter(id=category)
#             if qs[0].parent:
#                 items = Image.objects.filter(variant__product__category = qs[0]).filter(variant__is_main_variant=True).filter(is_main=True)
#             else:
#                 child_categories1 = []
#                 cats = Category.objects.all()
#                 for cat in cats:
#                     if cat.parent:
#                         if qs[0].title == cat.title:
#                             child_categories1.append(cat)
#                 child_categories2 = Category.objects.filter(parent=qs[0])

#                 items_list = []
#                 items = []

#                 for cat in child_categories1:
#                     items_list.append(Image.objects.filter(variant__product__category = cat).filter(variant__is_main_variant=True).filter(is_main=True))
#                 for cat in child_categories2:
#                     items_list.append(Image.objects.filter(variant__product__category = cat).filter(variant__is_main_variant=True).filter(is_main=True))

#                 for item_list in items_list:
#                     for item in item_list:
#                         items.append(item)

#         elif category is None and color is not None:
#             items = Image.objects.filter(is_main=True).filter(variant__color__title__icontains=color)

#         data = self.get_serializer(items, many=True).data
        
#         return Response(data)




# class CategoryApiView(APIView):

#     def get(self, request, *args, **kwargs):
#         category = request.query_params.get('category')
#         color = request.query_params.get('color')

#         queryset = Image.objects.filter(variant__is_main_variant=True).filter(is_main=True)

#         filters = Q()

#         if category:
#             filters &= Q(variant__product__category__id=int(category))
#         if color:
#             filters &= Q(variant__color__title__icontains=color)

#         queryset = Image.objects.filter(filters)
#         print(queryset)
        

#         serializer = GetImageSerializer(queryset, context={"request": self.request}, many=True)

#         return JsonResponse(serializer.data, safe=False)


# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]

# Function API views
# class VariantApiView(APIView):

#     def get(self, *args, **kwargs):
#         variants = Variant.objects.all()
#         serializer = GetVariantSerializer(variants, context={"request": self.request}, many=True)

#         return JsonResponse(serializer.data, safe=False)
    
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = PostVariantSerializer(data=data)
#         print(data)
#         if serializer.is_valid():
#             print('salam')
#             serializer.save()
#             return JsonResponse(serializer.data, status=201, safe=False)
#         else:
#             return JsonResponse(serializer.errors, status=400, safe=False)


# Function API views
# class ImageApiView(APIView):

#     def get(self, *args, **kwargs):
#         images = Image.objects.all()
#         serializer =  GetImageSerializer(images, context={"request": self.request}, many=True)

#         return JsonResponse(serializer.data, safe=False)