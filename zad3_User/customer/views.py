from django.shortcuts import render
from django.contrib import messages
from .models import Basket


def produce_customer(reqeust):
    if reqeust.method == "POST":
        Basket.objects.create()

        messages.success(reqeust, f"New record has been created")
    return render(reqeust, 'customer/produce_customer.html')
