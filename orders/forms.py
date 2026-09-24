from django import forms


class CheckoutForm(forms.Form):

    customer_name = forms.CharField(
        max_length=200
    )

    phone = forms.CharField(
        max_length=20
    )

    address = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

    delivery_type = forms.ChoiceField(
        choices=[
            ("pickup", "Retiro"),
            ("delivery", "Delivery")
        ]
    )