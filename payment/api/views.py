from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostAddToCartSerializer, GetCartListSerializer
from ..models import CartItem


class AddToCart(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PostAddToCartSerializer(data=data)
        if serializer.is_valid():
            existing_item = CartItem.objects.filter(cart=request.data["cart"], variant=request.data["variant"], size=request.data["size"]).first()
            if existing_item:
                existing_item.quantity += int(request.data["quantity"])
                existing_item.save()
                
            else:
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class GenericViewSerializerMixin:
    def get_serializer_class(self):
            return self.serializers_classes[self.request.method]


# class CartRemoveApiView(GenericViewSerializerMixin, RetrieveUpdateDestroyAPIView):
#     queryset = CartItem.objects.all()
#     serializers_classes = {
#         "DELETE": GetCartListSerializer,
#     }


class CartRemoveApiView(APIView):
    def delete(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        try:
            cart_item = CartItem.objects.get(pk=item_id)
        except CartItem.DoesNotExist:
            return Response({"detail": f"Cart item with id {item_id} not found"}, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()
        cart_item.cart.calculate_total_price()

        return Response({"detail": f"Cart item with id {item_id} successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


class CartListApiView(ListAPIView):
    serializer_class = GetCartListSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = CartItem.objects.filter(cart__user__id=user_id).filter(done=False)
        else:
            queryset = CartItem.objects.all()

        return queryset