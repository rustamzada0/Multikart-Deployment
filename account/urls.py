from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('login/', sign_in, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', sign_up, name='register'),
    path('vendor-profile/', vendor_profile, name='vendor-profile'),
    path('wishlist/', wishlist, name='wishlist'),
    path('logout/', logout_request, name='logout'),
    path('remove/<int:variant_id>/', remove_item, name='remove_item'),
    path('add/<int:variant_id>/', add_item, name='add_item'),
    path('activate/<str:uidb64>/<str:token>/', ActiveAccountView.as_view(), name='activate'),
    # path('forget-pwd/', forget_pwd, name='forget-pwd'),

]