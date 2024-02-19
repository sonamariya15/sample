from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate
from django.contrib import messages
from  datetime import datetime

# Create your views here.
def index(request):

    return render(request,"index.html")
def login(request):
    if request.POST:
        email=request.POST["email"]
        password=request.POST["password"]

        user=authenticate(username=email,password=password)

        if user:
            if user.is_active:
                if user.is_superuser:
                    return redirect("/adminhome")
                elif user.type=="user":
                    request.session["email"]=email
                    a=Registration_user.objects.get(email=email)
                    request.session['id']=a.id
                   
                    return redirect("/userhome")
                
                
   



    return render(request,"login.html")
def registration(request):
    

    if request.POST:
        name=request.POST["name"]
        contact=request.POST["contact"]
        email=request.POST["email"]
        profile=request.FILES["profile"]
        address=request.POST["address"]
        password=request.POST["password"]

        messages.info(request,"Registration Successfull")

        x=Logintable.objects.create_user(username=email,password=password,type="user")
        x.save()
        u=Registration_user.objects.create(name=name,contact=contact,email=email,profile=profile,address=address,password=password,userid=x)
        u.save()

    
    return render(request,"registration.html")

# ################  admin home #######################
def adminhome(request):
    

    return render(request,"admin/adminhome.html")
def manage_user(request):
    user=Registration_user.objects.all()


    

    return render(request,"admin/manage_user.html",{"user":user})
def deleuser(request):
    userid=request.GET.get('id')
    u=Logintable.objects.get(id=userid)
    u.delete()
    messages.info(request,"Removed Successfully")



    return redirect("/manage_user")
def view_feedback(request):
    
    data=Feedback.objects.all()
    

    return render(request,"admin/view_feedback.html",{"data":data})
def add_decor(request):
    if request.POST:
        name=request.POST["name"]
        desc=request.POST["desc"]
        price=request.POST["price"]
        image=request.FILES["image"]
        u=DecorItems.objects.create(name=name,desc=desc,price=price,image=image)
        u.save()
        messages.info(request,"Added Successfully")


    

    return render(request,"admin/add_decor.html")
def add_kitchen_items(request):
    if request.POST:
        name=request.POST["name"]
        desc=request.POST["desc"]
        price=request.POST["price"]
        image=request.FILES["image"]
        u=KitchenAppliances.objects.create(name=name,desc=desc,price=price,image=image)
        u.save()
        messages.info(request,"Added Successfully")
    

    return render(request,"admin/add_kitchen.html")
def manage_all_product (request):
    item=DecorItems.objects.all()
    kitchen=KitchenAppliances.objects.all()

    return render(request,"admin/manage_all_product.html",{"item":item ,"kitchen":kitchen})
def deleitem(request):
    userid=request.GET.get('id')
    u=DecorItems.objects.get(id=userid)
    u.delete()
    
    messages.info(request,"Removed Successfully")

    return redirect("/manage_all_product")
def delekit(request):
    userid=request.GET.get('id')
    u=KitchenAppliances.objects.get(id=userid)
    u.delete()
    messages.info(request,"Removed Successfully")
    return redirect("/manage_all_product")
# def update(request):
    
#     return redirect("/manage_all_product")
def view_request(request):
   
    user=Request.objects.all()



    return render(request,"admin/view_request.html",{"user":user})
def accept(request):
     a=request.GET.get('id')
     p=Request.objects.get(id=a)
     p.status="accept"
     p.save()
     return redirect("/view_request")
def quarter (request):
     a=request.GET.get('id')
     p=Request.objects.get(id=a)
     p.status="25%"
     p.save()
     return redirect("/view_request")

     
     
def  half(request):
     a=request.GET.get('id')
     p=Request.objects.get(id=a)
     p.status="50%"
     p.save()
     
     return redirect("/view_request")
def third (request):
     a=request.GET.get('id')
     p=Request.objects.get(id=a)
     p.status="75%"
     p.save()
     
     return redirect("/view_request")

def complete(request):
     a=request.GET.get('id')
     p=Request.objects.get(id=a)
     p.status="complete"
     p.save()
     
     return redirect("/view_request")
def view_booking(request):
    data=Booking.objects.all()
    

    return render(request,"admin/view_booking.html",{"data":data})
def view_payment(request):
    data=Payment.objects.all()
    

    return render(request,"admin/view_payment.html",{"data":data})


########## user home ###########
def userhome(request):
    id=request.session["id"]
    user=Registration_user.objects.get(id=id)

    return render(request,"user/userhome.html",{"user":user})

def view_all_decoritems(request):
    item=DecorItems.objects.all()
   

    return render(request,"user/view_all_decoritems.html",{"item":item })
def view_all_kitchenappliances(request):
    kitchen=KitchenAppliances.objects.all()

    return render(request,"user/view_all_kitchen.html",{"kitchen":kitchen})

def request_product(request):
    
    
   
    id=request.session["id"]
    user=Registration_user.objects.get(id=id)
    if request.POST:
        name=request.POST['name']
        image=request.FILES['image']
        date=request.POST['date']
        current_date=datetime.now()

        messages.info(request,"Request Shared Successfully")
        requests=Request.objects.create(name=name,image=image,date=date,current_date=current_date,userid=user)
        requests.save()

    return render(request,"user/request_product.html")

def view_manage_request(request):
    id=request.session['id']
    uid=Registration_user.objects.get(id=id)
    user=Request.objects.filter(userid=uid)

    return render(request,"user/view_manage_request.html",{"user":user})
def feedback(request):

    rid=request.GET.get('id')
    e=Request.objects.get(id=rid)
    id=request.session['id']
    user=Registration_user.objects.get(id=id)
    if request.POST:
        title=request.POST['title']
        desc=request.POST['desc']
        messages.info(request,"Feedback Shared  Successfully")
        feedback=Feedback.objects.create(title=title,desc=desc,rid=e,userid=user)
        feedback.save()

    return render(request,"user/feedback.html")

def booking_decoritems(request):
    tid=request.GET.get('id')
    deid=DecorItems.objects.get(id=tid)

    id=request.session['id']
    uid=Registration_user.objects.get(id=id)
    

    if request.POST:
        
        desc=request.POST['desc']
        date=datetime.now()
        book=Booking.objects.create(desc=desc,date=date,userid=uid,deid=deid)
        book.save()
        messages.info(request,"Booked Successfully")
        return redirect("/payment_decor")
       

    

    return render(request,"user/booking_decor.html",{"uid":uid})
def booking_kitchenappliances(request):
    tid=request.GET.get('id')
    kitid=KitchenAppliances.objects.get(id=tid)

    id=request.session['id']
    uid=Registration_user.objects.get(id=id)


    if request.POST:
        
        desc=request.POST['desc']
        date=datetime.now()
        book=Booking.objects.create(desc=desc,date=date,userid=uid,kitid=kitid)
        book.save()
        messages.info(request,"Booked Successfully")

        return redirect("/payment_kitchen")


    return render(request,"user/booking_kitchen.html",{"uid":uid})
def payment_kitchen(request):
   
   

    id=request.session['id']
    
    userid=Registration_user.objects.get(id=id)
    

    if request.POST:
        name=request.POST['name']
        current_date=datetime.now()
        book=Payment.objects.create(name=name,current_date=current_date,userid=userid)
        book.save()



    return render(request,"user/payment_kitchen.html")
def payment_decor(request):
     id=request.session['id']
    
     userid=Registration_user.objects.get(id=id)
    

     if request.POST:
        name=request.POST['name']
        current_date=datetime.now()
        book=Payment.objects.create(name=name,current_date=current_date,userid=userid)
        book.save()

     
     return render(request,"user/payment_decor.html")
def view_bookinguser(request):
    id=request.session['id']
    uid=Registration_user.objects.get(id=id)
    
    data=Booking.objects.filter(userid=uid)


   
     
    return render(request,"user/view_bookinguser.html",{"data":data})
def delebooking(request):
    userid=request.GET.get('id')
    u=Booking.objects.get(id=userid)
    u.delete()
    
   

    return redirect("/view_bookinguser")
