// Cart management using localStorage (replicating Django Cart logic)

const CART_STORAGE_KEY = 'churros_cart';

export function getCart() {
    try {
        const cart = localStorage.getItem(CART_STORAGE_KEY);
        return cart ? JSON.parse(cart) : {};
    } catch (e) {
        console.error('Error reading cart from localStorage', e);
        return {};
    }
}

export function saveCart(cart) {
    try {
        localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(cart));
        window.dispatchEvent(new Event('cartUpdated'));
    } catch (e) {
        console.error('Error saving cart to localStorage', e);
    }
}

export function addToCart(product, quantity = 1, extraIds = [], portion = null, extrasObjs = []) {
    const cart = getCart();
    
    // Sort and clean extra_ids
    extraIds = extraIds.map(id => parseInt(id)).filter(id => !isNaN(id));
    extraIds.sort((a, b) => a - b);

    let unitPrice = portion ? parseFloat(portion.price) : parseFloat(product.price);
    let itemName = portion ? `${product.name} (${portion.name})` : product.name;

    // Add extras prices
    if (extrasObjs && extrasObjs.length > 0) {
        extrasObjs.forEach(ext => {
            unitPrice += parseFloat(ext.price || 0);
        });
        const extNames = extrasObjs.map(ext => ext.name).join(', ');
        itemName = `${itemName} (+ ${extNames})`;
    }

    // Build unique cart key (matching Django logic: id_port_X_ext_Y-Z)
    const keyParts = [product.id];
    if (portion) {
        keyParts.push(`port_${portion.id}`);
    }
    if (extraIds.length > 0) {
        keyParts.push(`ext_${extraIds.join('-')}`);
    }
    const cartKey = keyParts.join('_');

    quantity = parseInt(quantity) || 1;

    if (!cart[cartKey]) {
        cart[cartKey] = {
            name: itemName,
            price: unitPrice,
            quantity: quantity,
            productId: product.id,
            image: product.image,
            portionName: portion ? portion.name : null,
            extras: extrasObjs.map(e => e.name)
        };
    } else {
        cart[cartKey].quantity += quantity;
    }

    saveCart(cart);
    return cartKey;
}

export function removeFromCart(cartKey) {
    const cart = getCart();
    if (cart[cartKey]) {
        delete cart[cartKey];
        saveCart(cart);
    }
}

export function updateQuantity(cartKey, quantity) {
    const cart = getCart();
    quantity = parseInt(quantity);
    if (cart[cartKey]) {
        if (quantity <= 0) {
            delete cart[cartKey];
        } else {
            cart[cartKey].quantity = quantity;
        }
        saveCart(cart);
    }
}

export function clearCart() {
    localStorage.removeItem(CART_STORAGE_KEY);
    window.dispatchEvent(new Event('cartUpdated'));
}

export function getCartTotal() {
    const cart = getCart();
    let total = 0;
    Object.values(cart).forEach(item => {
        total += item.price * item.quantity;
    });
    return total;
}

export function getCartCount() {
    const cart = getCart();
    let count = 0;
    Object.values(cart).forEach(item => {
        count += item.quantity;
    });
    return count;
}
