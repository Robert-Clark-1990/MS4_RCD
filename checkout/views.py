from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': "pk_test_51IdXmsDPZHBXw4mZZ78adeN6L5KyXJXMNzceU9ndSvewqG5qKKR1EhqdYqlkM1V9SMS0b4xrIp8jJapBYmj9NiVL00bPeQgTzj"
    }

    return render(request, template, context)
