from datetime import datetime
from django.shortcuts import redirect

from paymentSystems.bitgo import *
from paymentSystems.models import *


def buy(request, cheat):
    keys = Key.objects.filter(cheat__id=cheat, purchase=None, duration=int(request.GET.get('duration')))
    if len(keys) <= int(request.GET.get('quantity')):
        return redirect(f'/cheats/{cheat}/?error=OutOfStock')

    key_price = Price.objects.get(cheat__id=cheat, duration=int(request.GET.get('duration')))
    price = key_price.price*int(request.GET.get('quantity')) #Final price

    method = request.GET.get('payment')

    purchase = Purchase(user = request.user, date=datetime.now(), payment_method=method, status="Pending")
    purchase.save()
    if method == "Bitcoin":
        bitgo = Bitgo()
        wallet = bitgo.get_wallet()

        address = wallet.create_address()

        purchase.payment.bitcoin = BitcoinPayment(address=address)
        purchase.payment.bitcoin.save()

    return redirect(f'/purchases/?open={purchase.id}')