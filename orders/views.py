import urllib.parse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CheckoutForm
from .models import Order, OrderItem
from cart.cart import Cart

# Create your views here.

def checkout(request):
    cart = Cart(request)
    if not cart.cart:
        return redirect('cart_detail')

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                customer_name=form.cleaned_data["customer_name"],
                phone=form.cleaned_data["phone"],
                address=form.cleaned_data.get("address", ""),
                delivery_type=form.cleaned_data["delivery_type"],
                total=cart.get_total_price()
            )

            for item in cart.cart.values():
                OrderItem.objects.create(
                    order=order,
                    product_name=item["name"],
                    quantity=item["quantity"],
                    unit_price=item["price"],
                    subtotal=item["price"] * item["quantity"]
                )

            cart.clear()
            return redirect('order_summary', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(
        request,
        "checkout.html",
        {"form": form}
    )

def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = order.items.all()

    delivery_label = "Delivery" if order.delivery_type == "delivery" else "Retiro en Local"

    products_text = ""
    for item in items:
        products_text += f"- {item.product_name} x {item.quantity}\n"

    whatsapp_message = f"""Hola Buen Apetito 🍩

Quiero confirmar el siguiente pedido:

Pedido #{order.id}

Cliente:
{order.customer_name}

Teléfono:
{order.phone}

Tipo entrega:
{delivery_label}
"""
    if order.delivery_type == "delivery":
        whatsapp_message += f"""
Dirección:
{order.address}
"""

    whatsapp_message += f"""
Productos:
{products_text}
Total:
${int(order.total)}

Adjuntaré el comprobante de transferencia.

Gracias."""

    encoded_message = urllib.parse.quote(whatsapp_message)
    whatsapp_url = f"https://wa.me/56928447989?text={encoded_message}"

    return render(
        request,
        "order_summary.html",
        {
            "order": order,
            "items": items,
            "delivery_label": delivery_label,
            "whatsapp_url": whatsapp_url,
        }
    )
