from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Product, ShopHistory

# Create your views here.
@login_required(login_url='student-login')
def home_view(request):
    return render(request, 'space/index.html')

def space_shop(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'space/space_shop.html', {'products': products})


def confirm_buy_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'space/confirm_buy_product.html', {'product': product})

def buy_product(request, id):
    product = Product.objects.get(id=id)
    ShopHistory.objects.create(product=product, student=request.user)
    return redirect('space-shop')

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'space/student_login.html')
