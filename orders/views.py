from django.shortcuts import render

# Create your views here.
def cart(r):
    return render(r,'ordersapp/cart.html')
def orders(r):
    return render(r,'ordersapp/orders.html')
def orderstatus(r):
    return render(r,'ordersapp/orderstatus.html')
