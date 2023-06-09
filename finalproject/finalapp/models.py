from django.db import models

# Create your models here.
class registration(models.Model):
    username=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    phone=models.IntegerField(max_length=100,null=True)
    usertype=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True,default="pending")

class shopreg(models.Model):
    shopname=models.CharField(max_length=100,null=True)
    ownername=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    phone=models.IntegerField(max_length=100,null=True)
    usertype=models.CharField(max_length=100,null=True,default="shop")
    industry=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True,default="pending")


class commonlogin(models.Model):
    email=models.EmailField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    usertype=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True,default="pending")


class products(models.Model):
    shopname=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to="products")
    pdtname=models.CharField(max_length=100,null=True)
    MRP=models.CharField(max_length=100,null=True)
    offerprice=models.IntegerField(max_length=100,null=True)
    discription=models.CharField(max_length=100,null=True)
    shopid=models.ForeignKey(shopreg,on_delete=models.CASCADE,null=True)

class cart(models.Model):
    productid=models.ForeignKey(products,on_delete=models.CASCADE,null=True)
    pdtname=models.CharField(max_length=100,null=True)
    shopid=models.ForeignKey(shopreg,on_delete=models.CASCADE,null=True)
    userid=models.ForeignKey(registration,on_delete=models.CASCADE,null=True)
    amount=models.IntegerField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True,default="pending")
    