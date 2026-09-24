from django.shortcuts import render, redirect
from products.models import Product
from .cart import Cart

# Create your views here.

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product)

    return redirect('product_list')

def cart_detail(request):
    cart = request.session.get('cart', {})

    return render(request, 'cart_detail.html', {'cart': cart})