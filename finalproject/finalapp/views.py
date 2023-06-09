from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import *

# Create your views here.
def adminindex(request):
    return render(request,"admin index.html")
def userindex(request):
    return render(request,"index.html")
def base(request):
    return render(request,"commonbase.html")
def register(request):
    if 'Register' in request.POST:
        username=request.POST.get("Username")
        password=request.POST.get("Password")
        email=request.POST.get("Email")
        phone=request.POST.get("Phone")
        usertype=request.POST.get("Usertype")
        insertqry=registration.objects.create(username=username,password=password,email=email,phone=phone,usertype=usertype)
        insertlogqry1=commonlogin.objects.create(email=email,password=password,usertype=usertype)
        insertlogqry1.save()
        insertqry.save()
    return render(request,"login.html")

def login(request):
    if 'Login' in request.POST:
        email=request.POST.get("Email")
        password=request.POST.get("Password")
        status="approved"
        loginqry=commonlogin.objects.filter(email=email,password=password,status=status)#check this status
        print(loginqry)
        if loginqry[0].usertype=="admin":
            return HttpResponseRedirect("/admin index")
        if loginqry[0].usertype=="user":
            datau=registration.objects.filter(email=email)
            uid=datau[0].id
            request.session["userid"]=uid
            return HttpResponseRedirect("/userindex")
        if loginqry[0].usertype=="shop":
            data=shopreg.objects.filter(email=email)
            sid=data[0].id #storing shopid into a variable sid
            request.session["shopid"]=sid #shopid is a key,it is passing like a key value pair
            return HttpResponseRedirect("/individual shop page")
    return render(request,"login.html")

def shopregistration(request):
    if request.POST:
        shopname=request.POST.get("shopname")
        ownername=request.POST.get("ownername")
        password=request.POST.get("Password")
        email=request.POST.get("Email")
        phone=request.POST.get("Phone")
        industry=request.POST.get("industry")
        # print(shopname,password,email,phone,industry)
        shopinsert=shopreg.objects.create(ownername=ownername,shopname=shopname,password=password,phone=phone,email=email,usertype="shop",industry=industry)
        shopinsert.save()
        insertlogqry2=commonlogin.objects.create(email=email,password=password,usertype="shop")
        insertlogqry2.save()    
    return render(request,"shopregistration.html")

def individualshop(request):
    return render(request,"individualshop.html")

 
  
def adminview1(request):
    userdata=registration.objects.filter(status="pending")
    approvedusers=registration.objects.filter(status="approved")
    return render(request,"adminview1.html",{"data1":userdata,"data2":approvedusers})

def adminview2(request):
    shopdata=shopreg.objects.filter(status="pending")
    #print(shopdata)
    approvedshops=shopreg.objects.filter(status="approved")
    return render(request,"adminview2.html",{"data3":shopdata, "data4": approvedshops})

def adminapprove(request):
    id=request.GET['d1']
    status=request.GET['status']
    email=request.GET['email']
    if status=="approved":
        updateqry=registration.objects.filter(id=id).update(status="approved")
        updateqry2=commonlogin.objects.filter(email=email).update(status="approved")
    elif status=="delete":
        delqry=registration.objects.filter(id=id).delete()
        delqry2=commonlogin.objects.filter(email=email).delete()
    return HttpResponseRedirect("/adminview1")

def adminapprove2(request):
    id=request.GET['d2'] 
    status=request.GET['status']
    email=request.GET['email']
    if status=="approved":
        updateqry=shopreg.objects.filter(id=id).update(status="approved")
        updateqry2=commonlogin.objects.filter(email=email).update(status="approved")
    elif status=="delete":
        delqry=shopreg.objects.filter(id=id).delete()
        delqry2=commonlogin.objects.filter(email=email).delete()
    return HttpResponseRedirect("/adminview2")




def adminbase(request):
    return render(request,"adminbase.html")

    

def addproducts(request):
    # image=request.FILES['image']
    shopid=request.session['shopid']#is first shop id is key
    sid=shopreg.objects.get(id=shopid)#y not directly using shopid,instead of using sid,get method gives only particular value,not total row
    if request.POST:
        shopname=request.POST.get("shopname")
        image=request.FILES['image1']
        pdtname=request.POST.get('pdtname')
        MRP=request.POST.get('MRP')
        offerprice=request.POST.get('offerprice')
        discription=request.POST.get('discription')
        pdtdatainsert=products.objects.create(shopname=shopname,image=image,pdtname=pdtname,MRP=MRP,offerprice=offerprice,discription=discription,shopid=sid)
        pdtdatainsert.save()    
    return render(request,"addproducts.html")

def displayproducts(request):
    shopid=request.session['shopid']
    # sid=shopreg.objects.get(id=shopid)
    pdtdata=products.objects.filter(shopid=shopid)#filter gives complete row details,giving more than one rows,all raws having same feature
    # print(pdtdata)
    return render(request,"displayproducts.html",{"datax":pdtdata})

def updateproducts(request):
    id=request.GET['d5']
    pdtData=products.objects.get(id=id)
    if request.POST:
        shopname=request.POST.get("shopname")
        image=request.FILES['image1']
        pdtname=request.POST.get('pdtname')
        MRP=request.POST.get('MRP')
        offerprice=request.POST.get('offerprice')
        discription=request.POST.get('discription')
        pdtupdateqry=products.objects.get(id=id)
        pdtupdateqry.shopname=shopname
        pdtupdateqry.image=image
        pdtupdateqry.pdtname=pdtname
        pdtupdateqry.MRP=MRP
        pdtupdateqry.offerprice=offerprice
        pdtupdateqry.discription=discription
        pdtupdateqry.save()
        # .update(shopname=shopname,image=image,pdtname=pdtname,MRP=MRP,offerprice=offerprice,discription=discription)
        return HttpResponseRedirect("/displayproducts")
        
    return render(request,"updateproducts.html",{"pdtData":pdtData})

def deleteproduct(request):
    id=request.GET['d5']
    print(id)
    pdtData=products.objects.get(id=id).delete()
    return HttpResponseRedirect("/displayproducts")
    
def displayshops(request):
    shopdat=shopreg.objects.filter(status="approved")
    return render(request,"displayshops.html",{"shopdata":shopdat})
def userproductview(request):
    id=request.GET['d6']
    pdtdatafull=products.objects.filter(shopid=id)
    return render(request,"userproductview.html",{"datay":pdtdatafull,"id":id})

def addtocart(request):
    id=request.GET['d7']
    sid=request.GET['id']
    pid=products.objects.get(id=id)#to make the number into an object format using get
    productdata1=products.objects.filter(id=id)
    shopid=productdata1[0].shopid #its already a forigen key in the products table,so no error,can fetch data directly using dot method
    pdtname=productdata1[0].pdtname
    print(shopid)
    userid=request.session['userid']
    uid=registration.objects.get(id=userid)
    amount=productdata1[0].offerprice
    status="added"
    addqry=cart.objects.create(productid=pid,pdtname=pdtname,shopid=shopid,userid=uid,amount=amount,status=status)
    addqry.save()
    return HttpResponseRedirect("/userproductview?d6="+sid)
    # return render(request,"userproductview.html")

    
def checkout(request):
    uid=request.session['userid']
    cartdata=cart.objects.filter(status="added",userid=uid)
    sum=0
    length=len(cartdata)
    for i in range(0,length):
        sum+=cartdata[i].amount
    print("uuuuuuuuuuuuuuuuuu",sum)
    total=sum+15
    return render(request,"checkout.html",{"dataz":cartdata,"total":total})

def payment(request):
    msg=""
    uid=request.session['userid']
    total=request.GET['d8']
    if request.POST:
        cartdata=cart.objects.filter(status="added",userid=uid)
        for i in cartdata:
            cart.objects.filter(status="added",userid=uid).update(status="paid")
        msg=("payment successfull")
        HttpResponseRedirect("/myorders")
    return render(request,"payment.html",{"total":total,"msg":msg})

def myorders(request):
    uid=request.session['userid']
    orderlist=cart.objects.filter(status="paid",userid=uid)
    return render(request,"myorders.html",{"orderlist":orderlist})


def myorders2(request):
    uid=request.session['userid']
    orderlist=cart.objects.filter(status="paid",userid=uid)
    return render(request,"myorders2.html",{"orderlist":orderlist}) 

def ownershopview(request):
    shopid=request.session['shopid']
    shopdata3=shopreg.objects.filter(status="approved",id=shopid)
    return render(request,"ownershopview.html",{"shopdata3":shopdata3})

def ownershopupdate(request):
    shopid=request.GET['d9']
    shopdata=shopreg.objects.get(id=shopid)#while using get we obtain a single row of data
    print(shopdata)
    if request.POST:
        shopname=request.POST.get("shopname")
        ownername=request.POST.get("ownername")
        password=request.POST.get("password")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        industry=request.POST.get("industry")
        updateqry=shopreg.objects.filter(id=shopid).update(shopname=shopname,ownername=ownername,password=password,email=email,phone=phone,industry=industry)
        return HttpResponseRedirect("/ownershopview")
    return render(request,"ownershopupdate.html",{"shopdata":shopdata})

def userdataupdate(request):
    uid=request.session['userid']
    userdata=registration.objects.get(id=uid)
    if request.POST:
        username=request.POST.get("Username")
        password=request.POST.get("Password")
        email=request.POST.get("Email")
        phone=request.POST.get("Phone")
        usertype=request.POST.get("Usertype")
        updateqry=registration.objects.filter(id=uid).update(username=username,password=password,email=email,phone=phone,usertype=usertype)
        return HttpResponseRedirect("/userindex")

    return render(request,"userdataupdate.html",{"userdata":userdata})  

def home(request):
    request.session.clear()
    return render(request,"home.html")

def shopbase(request):
    return render(request,"shopbase.html")

def homebase(request):
    return render(request,"homebase.html")