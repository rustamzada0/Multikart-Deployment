"""
URL configuration for multikart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('admin/', admin.site.urls),
   

]
urlpatterns += i18n_patterns(
    path('',include('core.urls', namespace='core')),
    path('account/', include('account.urls', namespace='account')),
    path('product/', include('product.urls' , namespace='product')),
    path('payment/', include('payment.urls', namespace='payment')),

    path('oauth/', include('social_django.urls', namespace='social')),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="forget_pwd.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('api/', include('product.api.urls', namespace='product_api')),
    path('api/', include('core.api.urls', namespace='core_api')),
    path('api/', include('payment.api.urls', namespace='payment_api')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    prefix_default_language=False
)

handler404 = 'core.views.error'


# urlpatterns += static(settings.STATIC_URL,documnet_root=settings.STATIC_ROOT)