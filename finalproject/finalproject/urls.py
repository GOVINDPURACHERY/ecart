"""
URL configuration for finalproject project.

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
from finalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin index/',views.adminindex),
    path('userindex/',views.userindex),
    # path('',views.userindex),
    path('commonbase/',views.base),
    path('adminbase/',views.adminbase),
    path('user or admin registration/',views.register),
    path('login/',views.login),
    # path('',views.login),
    # path('adminlogin/',views.login),
    path('shopregistration/',views.shopregistration),
    path('individual shop page/',views.individualshop),
    path('adminview1/',views.adminview1),
    path('adminapproval/',views.adminapprove),
    path('adminview2/',views.adminview2),
    path('adminapproval2/',views.adminapprove2),
    path('addproducts/',views.addproducts),
    path('displayproducts/',views.displayproducts),
    path('updateproducts/',views.updateproducts),
    path('deleteproduct/',views.deleteproduct),
    path('displayshops/',views.displayshops),
    path('userproductview/',views.userproductview),
    path('addtocart/',views.addtocart),
    path('checkout/',views.checkout),
    path('payment/',views.payment),
    path('myorders/',views.myorders),
    path('myorders2/',views.myorders2),
    path('ownershopview/',views.ownershopview),
    path('ownershopupdate/',views.ownershopupdate),
    path('userdataupdate/',views.userdataupdate),
    path('home/',views.home),
    path('',views.home),
    path('shopbase/',views.shopbase),
    path('homebase/',views.homebase),


]
