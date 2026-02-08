from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .cart import Cart



def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart/cart.html')

# Create your views here.
