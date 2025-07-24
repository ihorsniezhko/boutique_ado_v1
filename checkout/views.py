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
        'stripe_public_key': 'pk_test_51LsAVSDbrSAzYrzcRSLdMAqeaXZkUNLmV0cXhl70xgfdimMu6ZPgf6orKSjM3KQR2JfEfxPjISBRhUV6xXX5WnyA00ZksvPBi2pk_test_51RoRLDJg4sTKuryHFOlfLrXuzvcEqsaaXlVzlYPm7zIsS3FTDpQHY7I01bVZA4lyyI7iUgpax34Rb3Qm0wDe06VA00IMFO63JC',
        'client_secret': '',
    }

    return render(request, template, context)