// Global app initialization (cart badge updater, bottom nav, floating whatsapp)
import { getCartCount } from './cart.js';

export function updateCartBadge() {
    const count = getCartCount();
    const badges = document.querySelectorAll('.cart-badge');
    badges.forEach(badge => {
        badge.textContent = count;
        badge.style.display = count > 0 ? 'flex' : 'none';
    });
}

function renderAppShell() {
    // Determine active page
    const path = window.location.pathname;
    const isHome = path.endsWith('index.html') || path === '/' || path.endsWith('/');
    const isCatalog = path.includes('catalog.html');
    const isCart = path.includes('cart.html') || path.includes('checkout.html') || path.includes('summary.html');

    // Inject Bottom Navigation Bar if not already present
    if (!document.querySelector('.bottom-nav')) {
        const bottomNav = document.createElement('nav');
        bottomNav.className = 'bottom-nav';
        bottomNav.innerHTML = `
            <a href="index.html" class="bottom-nav-item ${isHome ? 'active' : ''}">
                <span class="icon">🏠</span>
                <span>Inicio</span>
            </a>
            <a href="catalog.html" class="bottom-nav-item ${isCatalog ? 'active' : ''}">
                <span class="icon">📖</span>
                <span>Menú</span>
            </a>
            <a href="cart.html" class="bottom-nav-item ${isCart ? 'active' : ''}">
                <span class="icon">🛒</span>
                <span>Carrito</span>
            </a>
            <a href="catalog.html" class="bottom-nav-item">
                <span class="icon">👤</span>
                <span>Perfil</span>
            </a>
        `;
        document.body.appendChild(bottomNav);
    }

    // Inject Floating WhatsApp Widget if not present
    if (!document.querySelector('.floating-whatsapp')) {
        const whatsappBtn = document.createElement('a');
        whatsappBtn.href = 'https://wa.me/56928447989?text=Hola%20Buen%20Apetito%20🍩%20Quiero%20hacer%20un%20pedido.';
        whatsappBtn.target = '_blank';
        whatsappBtn.className = 'floating-whatsapp';
        whatsappBtn.innerHTML = '💬';
        whatsappBtn.title = 'Chatea con nosotros';
        document.body.appendChild(whatsappBtn);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateCartBadge();
    renderAppShell();
    window.addEventListener('cartUpdated', updateCartBadge);
});
