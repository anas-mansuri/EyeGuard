from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('contact/',views.contact,name="ShopContact")
]
