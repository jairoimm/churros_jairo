from django import forms


class CheckoutForm(forms.Form):

    customer_name = forms.CharField(
        max_length=200,
        label="Nombre y Apellido"
    )

    phone = forms.CharField(
        max_length=20,
        label="Teléfono / Celular"
    )

    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ej: Av. Concha y Toro #1234, Depto 45'}),
        label="Dirección de Entrega (Calle, número, depto / comuna)"
    )

    delivery_type = forms.ChoiceField(
        choices=[
            ("pickup", "Retiro en Local"),
            ("delivery", "Delivery (Despacho a domicilio)")
        ],
        label="Tipo de Entrega"
    )
