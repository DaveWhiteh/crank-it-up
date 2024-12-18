from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Pc5ImCwIwEettPLLrVzAMSAmJ21GmqupXHKS3xIysSzSSQLIStIKrnBHxKE2GNbtQPiB7De3jCZIO4P7aFKK5jo00vphJzDfu',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
