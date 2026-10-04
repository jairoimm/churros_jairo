from products.models import Extra, ProductPortion


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, extra_ids=None, portion_id=None):
        if extra_ids is None:
            extra_ids = []
        
        extra_ids = [int(eid) for eid in extra_ids]
        extra_ids.sort()

        portion = None
        if portion_id:
            try:
                portion = ProductPortion.objects.get(id=portion_id, product=product, active=True)
            except ProductPortion.DoesNotExist:
                portion = None

        key_parts = [str(product.id)]
        if portion:
            key_parts.append(f"port_{portion.id}")
        if extra_ids:
            extras_str = "-".join(map(str, extra_ids))
            key_parts.append(f"ext_{extras_str}")
        
        cart_key = "_".join(key_parts)

        if portion:
            unit_price = float(portion.price)
            item_name = f"{product.name} ({portion.name})"
        else:
            unit_price = float(product.price)
            item_name = product.name

        extras_objs = Extra.objects.filter(id__in=extra_ids)
        for ext in extras_objs:
            unit_price += float(ext.price)

        if extras_objs:
            ext_names = ", ".join([ext.name for ext in extras_objs])
            item_name = f"{item_name} (+ {ext_names})"

        quantity = int(quantity)

        if cart_key not in self.cart:
            self.cart[cart_key] = {
                'name': item_name,
                'price': unit_price,
                'quantity': quantity,
            }
        else:
            self.cart[cart_key]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, cart_key):
        if cart_key in self.cart:
            del self.cart[cart_key]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.save()

    def get_total_price(self):
        total = 0
        for item in self.cart.values():
            total += item['price'] * item['quantity']
        return total
