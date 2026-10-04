from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart

# Create your views here.

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        extras = request.POST.getlist('extras')
        portion_id = request.POST.get('portion')
        cart.add(product, quantity=quantity, extra_ids=extras, portion_id=portion_id)
    else:
        cart.add(product, quantity=1)

    return redirect('cart_detail')

def remove_from_cart(request, cart_key):
    cart = Cart(request)
    cart.remove(cart_key)
    return redirect('cart_detail')

def cart_detail(request):

    cart = Cart(request)

    return render(
        request,
        "cart_detail.html",
        {
            "cart": cart.cart,
            "total": cart.get_total_price()
        }
    )
