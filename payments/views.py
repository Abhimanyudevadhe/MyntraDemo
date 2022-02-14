from django.shortcuts import render

# Create your views here.
def credit(r):
    return render(r,'paymentsapp/credit.html')
def debit(r):
    return render(r,'paymentsapp/debit.html')
def EMI(r):
    return render(r,'paymentsapp/EMI.html')
def internet(r):
    return render(r,'paymentsapp/internet.html')
