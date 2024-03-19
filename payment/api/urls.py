from django.urls import path
from .views import AddToCart, CartListApiView, CartRemoveApiView


app_name = 'payment_api'

urlpatterns = [
    path('addtocart/', AddToCart.as_view(), name = 'addtocart'),
    path('carts/', CartListApiView.as_view(), name = 'carts'),
    path('delete/<pk>', CartRemoveApiView.as_view(), name = 'delete'),
]