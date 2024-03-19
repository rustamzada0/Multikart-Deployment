from django.urls import path
from .views import SubsicriberApiView


app_name = 'core_api'

urlpatterns = [
    path('subs/', SubsicriberApiView.as_view(), name = 'subs'),
]