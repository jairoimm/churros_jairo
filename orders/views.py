from django.shortcuts import render
from .forms import CheckoutForm

# Create your views here.



def checkout(request):

    form = CheckoutForm()

    return render(
        request,
        "checkout.html",
        {"form": form}
    ) 