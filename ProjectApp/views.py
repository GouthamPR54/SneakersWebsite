from django.shortcuts import render
from ProjectApp.models import *
from datetime import date
from django.db import connection
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
def indexview(request):
    return render(request,'index.html')

def loginview(request):
    return render(request,'login.html')

def registerview(request):
    return render(request,'register.html')

def savenewuserview(request):
    username=request.POST["name"]
    email=request.POST["email"]
    contactno=request.POST["contact"]
    password=request.POST["password"]

    newuser=user(name=username,email=email,contact=contactno,password=password)
    newuser.save()
    return render(request,'login.html')

def processuserloginview(request):
    email=request.POST["email"]
    password=request.POST["password"]

    userdata=user.objects.filter(email=email)
    for userinfo in userdata:
        if userinfo.password==password:
            request.session["userid"]=userinfo.id
            return render(request,'home.html')
        else:
            return render(request,'login.html')

def showadminlogin(request):
    return render(request,'adminlogin.html')
        
def adminloginview(request):
    email=request.POST["email"]
    password=request.POST["password"]

    if email=="admin@123" and password=="admin":
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM projectapp_order JOIN projectapp_user ON projectapp_order.userid=projectapp_user.id JOIN projectapp_product ON projectapp_order.productid=projectapp_product.id")          
        row=cursor.fetchall()
        userlist=user.objects.all()
        return render(request,"adminhome.html",{'orderinfo':row,'userinfo':userlist})
    else:
        return render(request,"adminlogin.html")
    
def inactivatebtnview(request):
    userid=request.GET['userid']
    user.objects.filter(id=userid).update(is_active=0)
    userlist=user.objects.all()
    return render(request,'adminhome.html',{'userinfo':userlist})

def activatebtnview(request):
    userid=request.GET['userid']
    user.objects.filter(id=userid).update(is_active=1)
    userlist=user.objects.all()
    return render(request,'adminhome.html',{'userinfo':userlist})

def productpageview(request):
    return render(request,'productpage.html')

def addproductview(request):
    product_name=request.POST["Name"]
    product_description=request.POST["Description"]
    price=request.POST["Price"]
    quantity=request.POST["Quantity"]

    newproduct=product(Name=product_name,Description=product_description,Price=price,Quantity=quantity)
    newproduct.save()
    return render(request,'productpage.html')

def itempageview(request):
    products=product.objects.all()
    return render(request,'product.html',{'productinfo':products})

def addtocartview(request):
    pid=request.GET['productid']
    userid=request.session['userid']
    
    today=date.today()
    print(today)

    addcart=cart(productid=pid,userid=userid,date=today)
    addcart.save()
    products=product.objects.filter(id=pid)
    return render(request,'cartpage.html',{'productinfo':products})

def deletecartview(request):
     pid=request.GET['productid']
     carts=cart.objects.get(id=pid)
     carts.delete()
     return render(request,'cartpage.html')

def buydetailsview(request):
    pid=request.GET['productid']
    request.session["userproductid"]=pid
    products=product.objects.filter(id=pid)
    return render(request,'buydetails.html',{'productinfo':products})

def confirmview(request):
    userid=request.session['userid']
    pid=request.session["userproductid"]
    today=date.today()
    print(today)
    address=request.POST["address"]
    Quantity=request.POST["Quantity"]

    confirm=order(userid=userid,productid=pid,date=today,address=address,Quantity=Quantity)
    confirm.save()
    products=product.objects.all()
    return render(request,'buydetails.html',{'productinfo':products})
       
def aboutview(request):
    return render(request,'about.html')

def homeview(request):
    return render(request,'home.html')

def user_logout(request):
    logout(request)
    return redirect('index.html')