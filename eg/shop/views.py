from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request , 'shop/index.html')

def contact(request):
    return render(request,'shop/contact.html')

def account(request):
    return render(request,'shop/account.html')

def eyeglass(request):
    return render(request,'shop/eyeglass.html')

def goggle(request):
    return render(request,'shop/goggle.html')

def cart(request):
    return render(request,'shop/cart.html')

def checkout(request):
    return render(request,'shop/checkout.html')

def productframe(request):
    return render(request,'shop/productframe.html')

def productframe1(request):
    return render(request,'shop/productframe1.html')

def productframe2(request):
    return render(request,'shop/productframe2.html')

def productframe3(request):
    return render(request,'shop/productframe3.html')

def productframe4(request):
    return render(request,'shop/productframe4.html')

def shoplogin(request):
    return render(request,'shop/shoplogin.html')