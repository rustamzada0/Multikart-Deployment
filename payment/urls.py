from django.urls import path
from .views import cart, success, success_buy_now, landing2, BuyNowSession, CreateCheckoutSessionView, ProductLandingPageView

app_name = 'payment'

urlpatterns=[
    path('cart/', cart , name='cart'),
    path('landing2/<int:id>', landing2 , name='landing2'),
    path('buy-now/<int:id>', BuyNowSession.as_view() , name='buy-now'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view() , name='create-checkout-session'),
    path('landing-page', ProductLandingPageView.as_view() , name='landing-page'),
    path('success/', success , name='success'),
    path('success-buy-now/', success_buy_now , name='success-buy-now'),


]