from django.urls import path
from .views import home_view, space_shop

urlpatterns = [
    path('', home_view, name='home'),
    path('shop/', space_shop, name='space-shop'),
]