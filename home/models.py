from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Logintable(AbstractUser):
    type=models.CharField(null=True,max_length=40)
class Registration_user(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    contact=models.IntegerField()
    address=models.CharField(max_length=30)
    password=models.CharField(max_length=30,null=True)
    profile=models.ImageField(null=True)
    userid=models.ForeignKey(Logintable,on_delete=models.CASCADE,null=True)
class DecorItems(models.Model):
    name=models.CharField(max_length=30,null=True)
    desc=models.CharField(max_length=100,null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(null=True)
class KitchenAppliances(models.Model):
    name=models.CharField(max_length=30,null=True)
    desc=models.CharField(max_length=100,null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(null=True)


class Request(models.Model):
    name=models.CharField(max_length=20,null=True)
    image=models.ImageField(null=True)
    date=models.DateTimeField(null=True)
    current_date=models.DateTimeField(null=True)
    status=models.CharField(null=True,max_length=40,default="request")
    progress=models.CharField(null=True,max_length=40)
    userid=models.ForeignKey(Registration_user,on_delete=models.CASCADE,null=True)
class Feedback(models.Model):
    title=models.CharField(max_length=20,null=True)
    desc=models.CharField(max_length=500,null=True)
    rid=models.ForeignKey(Request,on_delete=models.CASCADE,null=True)
    userid=models.ForeignKey(Registration_user,on_delete=models.CASCADE,null=True)
    
class Booking(models.Model):
    desc=models.CharField(max_length=100,null=True)
    date=models.DateTimeField(null=True) 
    status=models.CharField(null=True,max_length=40,default="Booking Confirmed")
    userid=models.ForeignKey(Registration_user,on_delete=models.CASCADE,null=True)
    deid=models.ForeignKey(DecorItems,on_delete=models.CASCADE,null=True)
    kitid=models.ForeignKey(KitchenAppliances,on_delete=models.CASCADE,null=True)

class Payment(models.Model):
    name=models.CharField(max_length=100,null=True)
    current_date=models.DateField(null=True)
    status=models.CharField(null=True,max_length=40,default="Successful")
    userid=models.ForeignKey(Registration_user,on_delete=models.CASCADE,null=True)
    



    


