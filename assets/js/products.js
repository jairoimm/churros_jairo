// Products and Extras data loader
let productsCache = null;

export async function loadProductsData() {
    if (productsCache) return productsCache;
    try {
        const response = await fetch('data/products.json');
        if (!response.ok) throw new Error('No se pudo cargar products.json');
        productsCache = await response.json();
        return productsCache;
    } catch (error) {
        console.error('Error loading products:', error);
        return { products: [], extras: [] };
    }
}

export async function getProducts() {
    const data = await loadProductsData();
    return data.products || [];
}

export async function getProductById(id) {
    const data = await loadProductsData();
    return data.products.find(p => p.id === parseInt(id)) || null;
}

export async function getExtras() {
    const data = await loadProductsData();
    return data.extras || [];
}

export function formatPrice(amount) {
    return '$' + Number(amount).toLocaleString('es-CL');
}
