from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('categories/', category_page , name='category-page'),
    path('<path:path>/<slug:slug>', product_page, name='product-page')
]


#URL TAMAM
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)