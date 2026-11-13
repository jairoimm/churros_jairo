// Checkout data management using localStorage

const CHECKOUT_STORAGE_KEY = 'churros_checkout';

export function saveCheckoutData(data) {
    try {
        localStorage.setItem(CHECKOUT_STORAGE_KEY, JSON.stringify(data));
    } catch (e) {
        console.error('Error saving checkout data', e);
    }
}

export function getCheckoutData() {
    try {
        const data = localStorage.getItem(CHECKOUT_STORAGE_KEY);
        return data ? JSON.parse(data) : null;
    } catch (e) {
        console.error('Error reading checkout data', e);
        return null;
    }
}

export function clearCheckoutData() {
    localStorage.removeItem(CHECKOUT_STORAGE_KEY);
}
