from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from urllib.parse import urlparse
from django.db.models import F
from django.db.models.functions import Random
from .models import *
from account.models import *
from .forms import ReviewForm

# Create your views here.

# class CategoryPage(TemplateView):

#     template_name = 'category-page.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         categories = Category.objects.all()

#         for category in categories:
#             if category.get_absolute_url() == f"{self.kwargs.get('path')}":
#                 category = category
#                 break

#         images = Image.objects.filter(is_main=True)
#         variant = Variant.objects.all()

#         menu = MainPhotos.objects.get(id=6)
                
#         context['category'] = category
#         context['images'] = images
#         context['variant'] = variant
#         context['menu'] = menu

#         return context


def category_page(request):
    url = request.build_absolute_uri()
    parsed_url = urlparse(url)
    query_string = parsed_url.query

    new_items = Image.objects.filter(variant__is_main_variant=True,is_main=True,variant__new_status=True).order_by(Random()).annotate(dummy=F('id'))[:2]


    context = {
        'query_string': query_string,
        'new_items': new_items
    }

    return render(request , "category-page.html", context)


def product_page(request, path, slug):
    # Product
    variant = get_object_or_404(Variant, slug=slug)
    print(variant.star())
    if not variant.get_absolute_url() == f"{path}/{slug}":
        raise Http404
    images = Image.objects.filter(variant=variant).all()
    # End Product

    # Wishlist
    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(user=request.user)
        variants = []
        for wish in wishlist:
            variants.append(wish.variant) # wishlistdeki variantlar | html-da if variant in variants 
    else:
        if request.session.get("wishlist"):
            variants = request.session["wishlist"].split()
            variants = [int(i) for i in variants]
        else:
            variants = []
    # End Wishlist

    # Review
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.variant = variant
            review.save()
    else:
        form = ReviewForm()
    
    reviews = Review.objects.filter(variant=variant)

    # Related Products
    is_main_variant = Variant.objects.filter(product=variant.product).filter(is_main_variant=True).first()
    item_ = Image.objects.filter(variant=is_main_variant).first()
    related_items = Image.objects.filter(variant__is_main_variant=True).filter(variant__product__category = variant.product.category).filter(is_main=True)
    # End Related Products

    product_variant_list = Variant.objects.filter(product=variant.product)
    new_items = Image.objects.filter(variant__is_main_variant=True,is_main=True,variant__new_status=True).order_by(Random()).annotate(dummy=F('id'))[:3]


    context = {
        'variant': variant,
        'reviews': reviews,
        'images': images,
        'variants': variants,
        'related_items': related_items,
        'new_items':new_items,
        'item_': item_,
        'product_variant_list': product_variant_list,
        'form': form
    }
    return render(request, 'product-page.html', context)