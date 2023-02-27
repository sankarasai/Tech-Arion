from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('createuser', views.createuser.as_view(),name='createuser'),
    path('createproduct', views.createproduct.as_view(),name='createproduct'),
    path('createproductimg', views.createproductimg.as_view(),name='createproduct'),
    path('sendotp', views.sendotp.as_view(),name='sendotp'),
    path('loginwithotp', views.loginwithotp.as_view(),name='loginwithotp'),
    path('addcart', views.addcart.as_view(),name='loginwithotp'),
]