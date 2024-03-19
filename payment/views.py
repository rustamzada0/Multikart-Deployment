from typing import Any
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, JsonResponse
import stripe, random, json
from django.conf import settings
from django.views import View
from django.views.generic import TemplateView
from datetime import timedelta
from product.models import Variant, Image
from .models import Orders, CartItem
from account.models import Profile, User

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_key = 'sk_test_51OBLfsH1R08EYzAm6d6bZRsskKoO0MboWZV8TxTdvy1IRyAw4ChjRoHB2sMSnNJnLUgqSXvfTzA1IDIAJIQtqQMM00CG3rmbh7'

@login_required()
def cart(request):
#     if request.method == 'GET':
#         carts = Cart.objects.filter(user=request.user)
#         cart_list = []

#         toti = 0
#         for cart in carts:
#             cart_dict = {
#                 'product': cart.product,
#                 'quantity': cart.quantity,
#                 'total_price': cart.total_price,
#             }
#             toti += cart.total_price
#             cart_list.append(cart_dict)

#         context = {
#             'cart_list':cart_list,
#             'toti':toti
#         }
#     else:
#         pass
    
    return render(request , 'cart.html')


def success(request):

    CartItem.objects.filter(cart__user=request.user).update(done=True)
    items = CartItem.objects.filter(cart__user=request.user).filter(done=True)
    print(items)
    context = {
        'items':items
    }
    return render(request, 'order-success.html', context=context)


def success_buy_now(request):
    return render(request, 'order-success-2.html')


def cancel(request):
    return render(request, 'cancel.html')


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        # product_id = self.kwargs["pk"]
        # product = Variant.objects.filter(id=product_id)
        # "STRIPE_PUBLIC_KEY":settings.STRIPE_PUBLISHABLE_KEY
        cart_items = request.user.cart.items.all()
        items = []
        for cart_item in cart_items:
            item =             {
                'price_data': {
                    'currency': 'USD',
                    'unit_amount': int(float(cart_item.variant.actual_price)*100),
                    'product_data': {
                        'name': cart_item.variant.title,
                    },
                },
                'quantity': cart_item.quantity,
            }

            items.append(item)

        YOUR_DOMAIN = "http://127.0.0.1:8000/"
        checkout_session = stripe.checkout.Session.create(
        line_items=items,
        mode='payment',
        success_url=YOUR_DOMAIN + 'payment/success',
        cancel_url=YOUR_DOMAIN + 'payment/landing-page',
        )

        return redirect(checkout_session.url)


class BuyNowSession(View):
    def get(self, request, *args, **kwargs):
        buy_item =  Variant.objects.filter(id=kwargs.get('id')).first()
        item =             {
            'price_data': {
                'currency': 'USD',
                'unit_amount': int(float(buy_item.actual_price)*100),
                'product_data': {
                    'name': buy_item.title,
                },
            },
            'quantity': 1,
        }

        YOUR_DOMAIN = "http://127.0.0.1:8000/"
        checkout_session = stripe.checkout.Session.create(
        line_items=[item],
        mode='payment',
        success_url=YOUR_DOMAIN + 'payment/success-buy-now',
        cancel_url=YOUR_DOMAIN + 'payment/landing-page',
        )

        return redirect(checkout_session.url)
        

class ProductLandingPageView(TemplateView):
    
    template_name = 'landing.html'


def landing2(request, id):
    item = Variant.objects.filter(id=id).first()
    context = {
        'item':item
    }
    return render(request, 'landing2.html', context=context)