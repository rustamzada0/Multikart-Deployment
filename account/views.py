from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from account.tasks import send_confirmation_mail
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from .tokens import account_activation_token
from .forms import RegisterForm, ProfileForm
from product.models import Variant, Image
from .models import User, WishList
from payment.models import Cart

# Create your views here.

# def forget_pwd(request):
#     email = request.GET.get('email', "")
#     user = User.objects.filter(email=email).first()
#     if user:
#         send_confirmation_mail(user=user, current_site=get_current_site(request))

#     return render(request, 'forget_pwd.html')


def sign_in(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('account:profile'))
    else:
        error = ''
        if request.method == "POST":
            if '@' in request.POST['emailorusername']:
                email = request.POST['emailorusername']
                if User.objects.filter(email=email):
                    username = User.objects.get(email=email).username
                else: username=None
            else:
                username = request.POST['emailorusername']
                if User.objects.filter(username=username):
                    username = request.POST['emailorusername']
                else: username=None
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None: 
                login(request,user)
                messages.add_message(request, messages.SUCCESS, f"{('Welcome')} {str(username).upper()}!")
                return redirect(reverse_lazy("core:home"))
            else:  error=('Email or username or password wrong')
            
        return render(request,'login.html',  context={'error':error})


@login_required()
def profile(request):
    if request.method == 'POST':

        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.country = request.POST.get('selected_country')
            profile.save()
            return redirect(reverse_lazy("core:home"))
    else:
        form = ProfileForm()

    
    context = {
        'form': form
    }

    return render(request, 'profile.html', context)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('account:profile'))
    else:
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.is_active = False
                user.save()

                cart = Cart.objects.create(user=user)
                send_confirmation_mail(user=user, current_site=get_current_site(request))
                # current_site = get_current_site(request)
                # send_activate_link(user,current_site.domain,urlsafe_base64_encode(force_bytes(user.pk)), account_activation_token.make_token(user),)
                messages.add_message(request, messages.SUCCESS, f"Activation mail sended!")                
                return redirect(reverse_lazy('account:login'))
        return render(request,'register.html', context={'form':form})


class ActiveAccountView(View):
    def get(request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect(reverse_lazy("account:login"))
        else:
            return render(request, 'activation.html')


def vendor_profile(request):
    return render(request, 'vendor-profile.html')
        

def wishlist(request):
    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(user=request.user)
        
        if wishlist:
            images = []
            for wish in wishlist:
                images.append(Image.objects.filter(variant = wish.variant).filter(is_main=True).first())
        else:
            images = []
    else:
        if request.session.get("wishlist"):
            variants_ids = request.session["wishlist"].split()
            images = Image.objects.filter(variant__id__in=(variants_ids)).filter(is_main=True)
        else:
            images = []
            
    context = {
        'images': images
    }

    return render(request, 'wishlist.html', context)


def remove_item(request, variant_id):
    if request.user.is_authenticated:
        item = get_object_or_404(WishList, user=request.user, variant__id=variant_id)
        item.delete()
    else:
        if request.session.get("wishlist"):
            variants_ids = request.session["wishlist"].split()
            if str(variant_id) in variants_ids:
                variants_ids.remove(str(variant_id))
                request.session["wishlist"] = " ".join(variants_ids)
                request.session.modified = True

    messages.success(request, "The Product has been Removed from the Wishlist!")

    return redirect('account:wishlist')


def add_item(request, variant_id):
    if request.user.is_authenticated:
        variant = Variant.objects.filter(id=variant_id).first()
        wishlist = WishList.objects.filter(user=request.user)
        variants = []

        for wish in wishlist:
            variants.append(wish.variant)

        if variant in variants:
            return redirect('core:error')
        else:
            WishList.objects.create(user=request.user, variant=variant)
            
    else:
        existing_variant = request.session.get("wishlist", "")
        existing_variant = existing_variant + ' ' + str(variant_id)
        request.session["wishlist"] = existing_variant.strip()

    messages.success(request, _("The Product has been Added to the Wishlist!"))

    return redirect('account:wishlist')


def logout_request(request):
    logout(request)
    return redirect('account:login')


