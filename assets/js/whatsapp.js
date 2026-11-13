// WhatsApp message generator matching Django order summary format + payment/delivery policies

export function generateWhatsAppUrl(orderData, cartItems, totalAmount) {
    const phoneNumber = "56928447989";
    const isDelivery = orderData.delivery_type === "delivery";
    const deliveryLabel = isDelivery ? "Delivery (Solo dentro de Bajos de Mena)" : "Retiro en Local";

    let productsText = "";
    Object.values(cartItems).forEach(item => {
        productsText += `• ${item.name} x${item.quantity}\n`;
    });

    let message = `🍩 NUEVO PEDIDO\n\n`;
    message += `👤 Cliente:\n${orderData.customer_name}\n\n`;
    message += `📞 Teléfono:\n${orderData.phone}\n\n`;
    message += `🚚 Tipo entrega:\n${deliveryLabel}\n`;

    if (isDelivery && orderData.address) {
        message += `\n📍 Dirección (Bajos de Mena):\n${orderData.address}\n`;
    }

    message += `\n🛒 Productos\n\n${productsText}\n`;
    message += `💰 Total:\n$${Number(totalAmount).toLocaleString('es-CL')}\n\n`;
    
    if (isDelivery) {
        message += `💳 Método de pago:\nPago previo por transferencia para que ingrese a cocina.\n\n`;
    } else {
        message += `💳 Método de pago:\nEfectivo o transferencia al retirar.\n\n`;
    }

    message += `Gracias.`;

    const encodedMessage = encodeURIComponent(message);
    return `https://wa.me/${phoneNumber}?text=${encodedMessage}`;
}
