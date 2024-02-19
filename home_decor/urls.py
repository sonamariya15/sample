"""
URL configuration for home_decor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('registration',views.registration),
    path('login',views.login),
    path('adminhome',views.adminhome),
    path('manage_user',views.manage_user),
    path('deleuser',views.deleuser),
    path('view_feedback',views.view_feedback),
    path('add_decor',views.add_decor),
    path('add_kitchen_items',views.add_kitchen_items),
    path('view_request',views. view_request),
    path('accept',views.accept),
    path('quarter',views.quarter ),
    path('half',views.half ),
    path('third',views. third ),
    path('complete',views.complete),
    path('deleitem',views.deleitem),
    path('delekit',views. delekit),
    path('view_booking',views.view_booking),
    path('view_payment',views.view_payment),
    path('userhome',views.userhome),
    path('view_all_decoritems',views.view_all_decoritems),
    path('view_all_kitchenappliances',views.view_all_kitchenappliances),
    path('request_product',views.request_product),
    path('view_manage_request',views.view_manage_request),
    path('feedback',views.feedback),
    path('booking_decoritems',views.booking_decoritems),
    path('booking_kitchenappliances',views.booking_kitchenappliances),
    path('payment_decor',views.payment_decor),
    path('payment_kitchen',views.payment_kitchen),
    path('view_bookinguser',views.view_bookinguser),
    path('delebooking',views.delebooking),
   
    # path('update',views.update),
    # path('manage_all_product',views.manage_all_product),
   
]
