"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from ProjectApp.views import *
from ProjectApp.views import user_logout 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',indexview),
    path('login/',loginview),
    path('home/',homeview),
    path('register/',registerview),
    path('savenewuser/',savenewuserview),
    path('userlogin/',processuserloginview),
    path('getadminlogin/',showadminlogin),
    path('adminlogin/',adminloginview),
    path('inactivatebtn/',inactivatebtnview),
    path('activatebtn/',activatebtnview),
    path("productpage/",productpageview),
    path("addproduct/",addproductview),
    path("product/",itempageview),
    path("addtocart/",addtocartview),
    path("buydetails/",buydetailsview),
    path("deletebtn/",deletecartview),
    path("confirm/",confirmview),
    path("about/",aboutview),
    path('logout/', user_logout, name='logout'),
]


