from django.urls import path
from .views import home_view, space_shop, confirm_buy_product, buy_product, student_login

urlpatterns = [
    path('', home_view, name='home'),
    path('shop/', space_shop, name='space-shop'),
    path('buy_product/<int:id>/', buy_product, name='buy_product'),
    path('confirm_product/<int:id>/', confirm_buy_product, name='confirm_product'),
    path('student_login/', student_login, name='student-login'),
]