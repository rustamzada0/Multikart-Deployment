from django.shortcuts import render
from .forms import ContactForm
from product.models import *
from .models import *

# Create your views here.
def home(request):
    items = Image.objects.filter(variant__is_main_variant=True).filter(is_main=True)
    main_photos_men = MainPhotos.objects.get(id=1)
    main_photos_women = MainPhotos.objects.get(id=2)
    
    context = {
        'main_photos_men':main_photos_men,
        'main_photos_women':main_photos_women,

        'items': items,
    }
    
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact.html', context=context)


def search(request):
    search = request.GET.get('search', "")

    if search:
        images = Image.objects.filter(variant__title__icontains=search).filter(is_main=True)
    else:
        images = []

    return render(request, 'search.html', {'images': images})


def faq(request):
    return render(request, 'faq.html')


def about_page(request):
    return render(request, 'about-page.html')


def error(request, exception):
    return render(request, '404.html')