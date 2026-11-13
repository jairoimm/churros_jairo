// WhatsApp message generator matching Django order summary format

export function generateWhatsAppUrl(orderData, cartItems, totalAmount) {
    const phoneNumber = "56928447989";
    const deliveryLabel = orderData.delivery_type === "delivery" ? "Delivery (Despacho a domicilio)" : "Retiro en Local";

    let productsText = "";
    Object.values(cartItems).forEach(item => {
        productsText += `• ${item.name} x${item.quantity}\n`;
    });

    let message = `🍩 NUEVO PEDIDO\n\n`;
    message += `👤 Cliente:\n${orderData.customer_name}\n\n`;
    message += `📞 Teléfono:\n${orderData.phone}\n\n`;
    message += `🚚 Tipo entrega:\n${deliveryLabel}\n`;

    if (orderData.delivery_type === "delivery" && orderData.address) {
        message += `\n📍 Dirección:\n${orderData.address}\n`;
    }

    message += `\n🛒 Productos\n\n${productsText}\n`;
    message += `💰 Total:\n$${Number(totalAmount).toLocaleString('es-CL')}\n\n`;
    message += `Gracias.`;

    const encodedMessage = encodeURIComponent(message);
    return `https://wa.me/${phoneNumber}?text=${encodedMessage}`;
}
