from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search'),
    path('faq/', faq, name='faq'),
    path('about-page/', about_page, name='about-page'),
    path('error/', error, name='error'),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
