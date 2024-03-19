from django.urls import path
from .views import ProductDetailApiView, VariantDetailApiView, FilterApiView, AddToWishlist


app_name = 'product_api'

urlpatterns = [
    path('product/<int:pk>', ProductDetailApiView.as_view(), name = 'product'),
    path('variant/<int:pk>', VariantDetailApiView.as_view(), name = 'variant'),
    path('filter/', FilterApiView.as_view(), name = 'categories'),
    path('add-to-wishlist/', AddToWishlist.as_view(), name = 'add-to-wishlist'),
]