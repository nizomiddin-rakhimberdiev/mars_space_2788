from django.shortcuts import render

from .models import Product, ShopHistory

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def space_shop(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'space_shop.html', {'products': products})