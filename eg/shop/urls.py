from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.index,name="ShopHome"),
    path('contact/',views.contact,name="ShopContact"),
    path('account/',views.account,name="ShopAccount"),
    path('eyeglass/',views.eyeglass,name="ShopEyeGlass"),
    path('goggle/',views.goggle,name="ShopGoggle"),
    path('productframe/',views.productframe,name="ShopProductFrame"),
    path('productframe1/',views.productframe1,name="ShopProductFrame1"),
    path('productframe2/',views.productframe2,name="ShopProductFrame2"),
    path('productframe3/',views.productframe3,name="ShopProductFrame3"),
    path('productframe4/',views.productframe4,name="ShopProductFrame4"),
    path('productframe5/',views.productframe5,name="ShopProductFrame5"),
    path('cart/',views.cart,name="ShopCart"),
    path('checkout/',views.checkout,name="ShopCheckout"),
    path('shoplogin/',views.shoplogin,name="ShopLogin"),
    path('logout/',views.logout,name="ShopLogout"),
    path('contactlense/',views.contactlense,name="ShopContactLense"),
    path('lens/',views.lens,name="ShopLens"),
    path('prescription/', views.prescription, name="ShopPrescription"),
    path('wishlist/', views.wishlist, name="ShopWishlist"),
    path('', views.signup, name="ShopSignup"),
    path('thankyou/', views.thankyou, name="ShopThankyou"),
    path('Contactlenseframe1/', views.Contactlenseframe1, name="Contactlenseframe1"),
    path('Contactlenseframe2/', views.Contactlenseframe2, name="Contactlenseframe2"),
    path('Contactlenseframe3/', views.Contactlenseframe3, name="Contactlenseframe3"),
    path('Contactlenseframe4/', views.Contactlenseframe4, name="Contactlenseframe4"),
    path('Contactlenseframe5/', views.Contactlenseframe5, name="Contactlenseframe5"),
    path('Contactlenseframe6/', views.Contactlenseframe6, name="Contactlenseframe6"),
    path('Contactlenseframe7/', views.Contactlenseframe7, name="Contactlenseframe7"),
    path('Contactlenseframe8/', views.Contactlenseframe8, name="Contactlenseframe8"),
    path('Contactlenseframe9/', views.Contactlenseframe9, name="Contactlenseframe9"),

]
