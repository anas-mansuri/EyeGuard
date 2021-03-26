from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('contact/',views.contact,name="ShopContact"),
    path('account/',views.account,name="ShopAccount"),
    path('eyeglass/',views.eyeglass,name="ShopEyeGlass"),
    path('goggle/',views.goggle,name="ShopGoggle"),
    path('productframe/',views.productframe,name="ShopProductFrame"),
    path('productframe1/',views.productframe1,name="ShopProductFrame1"),
    path('productframe2/',views.productframe2,name="ShopProductFrame2"),
    path('productframe3/',views.productframe3,name="ShopProductFrame3"),
    path('productframe4/',views.productframe4,name="ShopProductFrame4"),
    path('cart/',views.cart,name="ShopCart"),
    path('checkout/',views.checkout,name="ShopCheckout"),
    path('shoplogin/',views.shoplogin,name="ShopLogin"),
]
