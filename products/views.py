from django.shortcuts import render

# Create your views here.
def bags(r):
    return render(r,'productsapp/bags.html')
def laptops(r):
    return render(r,'productsapp/laptops.html')
def mobiles(r):
    return render(r,'productsapp/mobiles.html')