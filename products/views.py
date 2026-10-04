from django.shortcuts import render, get_object_or_404
from .models import Product, Extra

# Create your views here.

def product_list(request):
    products = Product.objects.filter(active=True)
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, active=True)
    extras = product.extras.filter(active=True)
    portions = product.portions.filter(active=True)
    return render(request, 'product_detail.html', {'product': product, 'extras': extras, 'portions': portions})
