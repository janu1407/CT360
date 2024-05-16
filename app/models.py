from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=100,null=True)
    useremail = models.EmailField (null=True)
    password = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100 ,null=True)
    photo = models.FileField(upload_to="static/products")
    status = models.FileField(max_length=100,default="pending",null=True)
    class Meta:
        db_table = "User"


    

class AddProducts(models.Model):
    productname = models.CharField(max_length=50,null=True)
    productprice = models.PositiveIntegerField(null=True)
    productquantity = models.PositiveIntegerField(null=True)
    filedata = models.FileField(upload_to="static/products")
    owneremail = models.EmailField(null=True)
    today_date = models.DateField(null=True)
    product_desc = models.TextField(max_length=100,null=True)
    actualauantity = models.PositiveIntegerField(null=True)
    rentamount = models.PositiveIntegerField(null=True)
    communityname = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "AddProducts"

class UserOrder(models.Model):
    Product_Id = models.CharField(max_length=50,null=True)
    productname = models.CharField(max_length=50,null=True)
    productprice = models.PositiveIntegerField(null=True)
    productquantity = models.PositiveIntegerField(null=True)
    filedata = models.FileField(max_length=50,null=True)
    user_email = models.EmailField(max_length=50,null=True)
    product_cost = models.PositiveIntegerField(null=True)
    user_order_count = models.PositiveIntegerField(null=True)
    user_product_cost = models.PositiveIntegerField(null=True)
    owneremail = models.EmailField(null=True)
    status = models.CharField(max_length=50,default='pending')
    paymenttype = models.CharField(max_length=50,default="pending")
    class Meta:
        db_table = "UserOrder"


class Payment(models.Model):
    Productid = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    cardname = models.CharField(max_length=50,null=True)
    cardnumber=models.CharField(max_length=16,null=True)
    cvv= models.CharField(max_length=3,null=True)
    totalprice = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "Payment"
    


class RentAmount(models.Model):
    ProductId = models.CharField(max_length=100,null=True)
    useremail = models.EmailField(null=True)
    bookname = models.CharField(max_length=50,null=True)
    owneremail = models.CharField(max_length=100,null=True)
    rentamount = models.PositiveIntegerField(default=0,null=True)
    number = models.CharField(max_length=100,default='pending')
    status = models.CharField(max_length=20,default="pending")
    class Meta:
        db_table = "RentAmount"

    

class Community(models.Model):
    communityname = models.CharField(max_length=100,null=True)
    communitydescription = models.CharField(max_length=100,null=True)
    Communitytype =models.CharField(max_length=100,null=True)
    owneremail = models.EmailField(max_length=50,null=True)
    today_date = models.DateField(null=True)
    status = models.CharField(max_length=50,default='pending')
    class Meta:
        db_table = "Community"

class Member(models.Model):
    CommunityId = models.CharField(null=True,max_length=100)
    communityname = models.CharField(max_length=100,null=True)
    communitydescription = models.CharField(max_length=100,null=True)
    Communitytype =models.CharField(max_length=100,null=True)
    owneremail = models.EmailField(max_length=50,null=True)
    today_date = models.DateField(null=True)
    username = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    status = models.CharField(max_length=50,default='pending')
    class Meta:
        db_table = "Member"
    

    
