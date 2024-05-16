from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import *
from django.contrib.messages import *
from datetime import date
from django.core.exceptions import FieldError
from django.contrib import messages




# Templates
indexpage = "index.html"
userlogpage = "userlogin.html"
userregpage = "userreg.html"
userhomepage = "userhome.html"
myprofilepage = "profile.html"
addproductspage = "addproducts.html"
myproductspage = "myproducts.html"
allproductspage = "allproducts.html"
updateproductpage = "updateproduct.html"
userrequestspage = "userrequests.html"
paymentpage = "payment.html"
paypage = "pay.html"
viewallpaymentspage="viewallpayments.html"
myrentrequestspage ="myrentrequests.html"
fromrentrequestspage = "fromrentrequests.html"
rentpage = "rent.html"
searchproductpage = "search.html"
communitypage = 'community.html'
createcomminitypage = 'newcommunity.html'
viewcommunitypage = "viewcommunity.html"
viememberpage = "viewmember.html"
myproductsmores = "moreproduct.html"
allproductsmorepage = "allproductsmore.html"
viewmycard = "viewcard.html"
allproductshomepage = "all.html"
searchproductspage = "s.html"





# UserOrder.objects.all().delete()
# Home Page
def index(request):
    return render(request,indexpage)

def user(request):
    if request.method == "POST":
        useremail = request.POST["useremail"]
        password = request.POST["password"]
        print(useremail,password)
        dc = User.objects.filter(useremail=useremail,password=password).exists()
        if dc == True:
            request.session['useremail'] = useremail
            print(useremail)
            dc = User.objects.only('useremail').filter(useremail=useremail,password=password)
            x = []
            for i in dc:
                x.append(i.username)
            print(x)
            request.session['username']=x[0]
            dc = User.objects.filter(useremail=useremail,password=password)
            return render(request,userhomepage,{'dc':dc})
        else:
            messages.add_message(request, messages.INFO, 'Credentials are not valid')
            return render(request,userlogpage)
    return render(request,userlogpage)
   
def userreg(request):
    if request.method=="POST":
        username = request.POST['username']
        useremail = request.POST["useremail"]
        password = request.POST["password"]
        conpassword = request.POST["conpassword"]
        contact = request.POST["contact"]
        address = request.POST["address"]
        photo = request.FILES["photo"] 
        if password == conpassword:
            dc = User.objects.filter(useremail=useremail,password=password).exists()
            if dc == False:
                dc = User(username=username,useremail=useremail,password=password,contact=contact,address=address,photo=photo)
                dc.save()
                return redirect("user")
            else:
                messages.add_message(request, messages.INFO,'Account already exists with these credentials')
                return render(request,userregpage)
        else:
            messages.add_message(request, messages.INFO, "Passwords are not matching")
            return render(request,userregpage)
    return render(request,userregpage)

def viewmyprofile(request):
     my_profile = User.objects.filter(useremail= request.session['useremail'])
     return render(request,myprofilepage,{'my_profile':my_profile,'email':request.session['useremail']})

def myproducts(request):
    my_products = AddProducts.objects.filter(owneremail=request.session['useremail'])
    return render(request,myproductspage,{'my_products':my_products,'email':request.session['useremail']})

def myproductsmore(request,id):
    print(id)
    my_products = AddProducts.objects.filter(id=id, owneremail=request.session['useremail'])
    return render(request,myproductsmores,{'my_products':my_products,'email':request.session['useremail']})

def addproducts(request):
   
    
    communities = Community.objects.all()  # Retrieve all communities
    if request.method == "POST":
        # Retrieve form data
        productname = request.POST['productname']
        productprice = request.POST['productprice']
        productquantity = request.POST['productquantity']
        filedata = request.FILES['filedata']
        today_date = date.today()
        description = request.POST['description']
        rentamount = request.POST['rentamount']
        communityname = request.POST['communityname']  # Retrieve selected community name
        # Save product details to database
        dc = AddProducts(
            productname=productname,
            productprice=productprice,
            productquantity=productquantity,
            filedata=filedata,
            owneremail=request.session['useremail'],
            rentamount=rentamount,
            communityname=communityname,
            today_date=today_date,
            product_desc=description,
            actualauantity=productquantity
        )
        dc.save()
        messages.success(request, 'Product Added successfully.')
        return render(request, 'addproducts.html', {'email': request.session['useremail']})
    return render(request, 'addproducts.html', {'email': request.session['useremail'], 'communities': communities})

def allproductshome(request):
    all_products_data = AddProducts.objects.all()
    return render(request,allproductshomepage,{'all_data':all_products_data})

def allproducts(request):
    all_products_data = AddProducts.objects.exclude(owneremail = request.session['useremail'])
    return render(request,allproductspage,{'all_data':all_products_data,'email':request.session['useremail']})

def allproductsmore(request,id):
    print(id)
    print(request.session['useremail'])
    all_products_data = AddProducts.objects.filter(id=id)
    return render(request,allproductsmorepage,{'all_data':all_products_data,'email':request.session['useremail']})     

def searchproduct(request):
    if request.method=="POST":
        searchname = request.POST['searchproduct']
        print(searchname)
        dc = AddProducts.objects.filter(productname=searchname)
        print(dc)
        if dc !=[]:
            return render(request,searchproductpage,{'dc':dc})
        else:
            return render(request,searchproductpage)    
    return render(request,searchproductpage)

def searchproduct1(request):
    if request.method=="POST":
        searchname = request.POST['searchproduct']
        print(searchname)
        dc = AddProducts.objects.filter(productname=searchname)
        print(dc)
        if dc !=[]:
            return render(request,searchproductspage,{'dc':dc})
        else:
            return render(request,searchproductspage)    
    return render(request,searchproductspage)

def updateproduct(request,id):
    return render(request,updateproductpage,{'product_id':id,'email':request.session['useremail']})

def modifyproduct(request):
    if request.method == "POST":
        productid = request.POST['productid']
        productname = request.POST['productname']
        productprice = request.POST['productprice']
        productquantity = request.POST['productquantity']
        description = request.POST['description']
        filedata = request.FILES['filedata']
        # Assuming your primary key field is named 'id'
        update_date = AddProducts.objects.get(id=productid)
        update_date.productname = productname
        update_date.productprice = productprice
        update_date.productquantity = productquantity
        update_date.product_desc = description
        update_date.filedata = filedata
        update_date.save()
        return redirect("myproducts")

def deleteproduct(request,id):
    AddProducts.objects.filter(id=id).delete()
    return redirect("myproducts")

def addproduct(request, id):
    
    add_product = AddProducts.objects.filter(id=id)
    xc = [(i.id,i.productname, i.productprice, i.productquantity, i.owneremail,i.filedata) for i in add_product][0]
    ProductId = xc[0]
    Producname = xc[1]
    productprice = xc[2]
    productQuantity = xc[3]
    productowner = xc[4]
    useremail = request.session['useremail']
    filedata = xc[5]
    
    userorder = UserOrder.objects.filter(Product_Id=ProductId,owneremail=productowner, user_email=useremail).exists()
    
    if userorder:
        userorder = UserOrder.objects.filter(Product_Id=ProductId, owneremail=productowner, user_email=useremail )
        if userorder:
            for i in userorder:
                prouctid = i.Product_Id
                useremail =i.user_email
                cost = i.product_cost
                ordercount = i.user_order_count
                productcost = i.user_product_cost
                owneremail = i.owneremail
                
                
            userproductcount = ordercount
            df = UserOrder.objects.get(Product_Id=ProductId, user_email=useremail)
            df.productname = Producname
            df.productprice = productcost
            df.productquantity = ordercount
            df.user_order_count = df.user_order_count + 1
            df.user_product_cost = df.product_cost * df.user_order_count
            df.filedata = filedata
            df.save()
            print("-------")
            print(ProductId)
            dc = AddProducts.objects.get(id=ProductId)
            if dc.productquantity==0:
                messages.warning(request, "Stock Not Available")
                return redirect('allproducts')
            else:
                dc.productquantity = dc.productquantity - 1
                dc.save()
            return redirect('allproducts')
        else:
            messages.warning(request, "Stock Not Available")
            return redirect('allproducts')
    else:
        user_order_count = 1
        user_data = UserOrder(Product_Id=ProductId, user_email=useremail, product_cost=productprice,
                              user_order_count=user_order_count, user_product_cost=productprice,
                              owneremail=productowner)
        user_data.save()
        
        ab = AddProducts.objects.get(id=ProductId)
        ab.productquantity = ab.productquantity - user_order_count
        ab.save()
    return redirect("allproducts")

def productsremove(request,ProductId):
    print(ProductId)
    dc = UserOrder.objects.filter(Product_Id=ProductId,user_email=request.session['useremail']).exists()
    print(dc)
    if dc:
        dc = UserOrder.objects.get(Product_Id=ProductId,user_email=request.session['useremail'])
        dc.user_order_count - 1
        dc.product_cost - dc.user_order_count
        print(dc.product_cost)
        dc.save()
        db = AddProducts.objects.get(id=ProductId)

        print(db.actualauantity)
        print(db.productquantity)
        if db.productquantity<db.actualauantity:
            print("True")
            db.productquantity = db.productquantity+1
            db.save()
        else:
            messages.warning(request,"You didnt selected any order")
    else:
        messages.warning(request,"You didn't made any order")
    return redirect("allproducts")

def userrequests(request,id):
    users_order = UserOrder.objects.filter(Product_Id=id)
    return render(request,userrequestspage,{'users_order':users_order,'email':request.session['useremail']})

def acceptproduct(request,Product_Id,user_email):
    dc = UserOrder.objects.get(Product_Id=Product_Id,user_email=user_email)
    dc.status='accepted'
    dc.save()
    return redirect("userrequests",Product_Id)

def payment(request,ProductId):
    useremail=request.session['useremail']
    ds = UserOrder.objects.filter(Product_Id=ProductId,user_email=useremail,status='accepted').exists()
    if ds:
        dc = UserOrder.objects.get(Product_Id=ProductId,user_email=useremail,status='accepted')
        dc.paymenttype = "onlinepayment"
        dc.save()
        ds = UserOrder.objects.filter(Product_Id=ProductId,user_email=useremail,status='accepted')
        return render(request,paymentpage,{'ds':ds,'email':useremail})
    else:
        messages.warning(request,"Your not in the community and Your order is not accepted ")
        return redirect("allproducts")

def pay(request,Product_Id):
    print(Product_Id)
    dc = UserOrder.objects.filter(Product_Id=Product_Id,user_email=request.session['useremail'],status='accepted')
    for i in dc:
        abc = i.Product_Id,i.user_product_cost
    s = abc
    print(s)
    id= s[0]
    cost = s[1]
    print(id,cost)
    return render(request,paypage,{'dc':dc,'cost':cost,'id':id,'email':request.session['useremail']})

def allpayment(request):
    if request.method =="POST":
        productid = request.POST['productid']
        email=request.session['useremail']
        cardname = request.POST['cardname']
        cardnumber = request.POST['cardnumber']
        cvv = request.POST['cvv']
        totalprice = request.POST['totalprice']
        print(productid,email,cardname,cardnumber,cvv,totalprice)
        dc = Payment(Productid=productid,email=email,cardname=cardname,cardnumber=cardnumber,cvv=cvv,totalprice=totalprice)
        dc.save()
        return redirect("allproducts")

def viewallpayments(request,Product_Id):
    dc = Payment.objects.filter(Productid=Product_Id)
    return render(request,viewallpaymentspage,{'dc':dc,'email':request.session['useremail']})

from django.core.exceptions import FieldError

def rentamount(request, Product_Id):
    print(request.session['useremail'])
    user = User.objects.filter(useremail=request.session['useremail'])[0]
    df = User.objects.filter(id=user.id)
    ac = AddProducts.objects.filter(id=Product_Id)
    for i in ac:
        new_data = i.id, i.productname, i.owneremail, i.rentamount
    print(new_data)
    id = new_data[0]
    bookname = new_data[1]
    print(bookname)
    owneremail = new_data[2]
    rentamount = new_data[3]
    dc = RentAmount(ProductId=id, useremail=request.session['useremail'], bookname=bookname, owneremail=owneremail, rentamount=rentamount)
    dc.save()
    messages.warning(request, "Rent Request sent")
    return redirect("allproducts")

def myrentrequests(request):
    try:
        data = RentAmount.objects.filter(owneremail=request.session['useremail']) | RentAmount.objects.filter(useremail=request.session['useremail'])
        return render(request,myrentrequestspage,{'data':data,'email':request.session['useremail']})
    except:
        data = RentAmount.objects.filter(useremail=request.session['useremail'])
        return render(request,fromrentrequestspage,{'data':data,'email':request.session['useremail']})

def newaccept(request,ProductId):
    print(ProductId)
    dx = RentAmount.objects.exclude(useremail=request.session['useremail'],ProductId=ProductId, status='pending').first()
    dx.status = "accepted"
    dx.save()
    print(dx)
    return redirect("myrentrequests")

def Cashonpayment(request,ProductId):
    print()
    useremail=request.session['useremail']
    ds = UserOrder.objects.filter(Product_Id=ProductId,user_email=useremail,status='accepted').exists()
    if ds:
        dc = UserOrder.objects.get(Product_Id=ProductId,user_email=useremail,status='accepted')
        if dc.paymenttype=="onlinepayment":
            messages.warning(request,"request already sent as online payment")
            return render(request,paymentpage,{'email':useremail})            
        dc.paymenttype = "cashondelivery"
        dc.save()
        ds = UserOrder.objects.filter(Product_Id=ProductId, user_email=useremail, status='accepted')
        print(ds)  # Debugging: Print ds to check if it contains data
        return render(request,paymentpage,{'ds':ds,'email':useremail})
    else:
        messages.warning(request,"Your request is not accepted")
        return redirect("allproducts") 
    
def exchange(request, ProductId):
    print(ProductId)
    dc = UserOrder.objects.filter(Product_Id=ProductId,user_email=request.session['useremail']).exists()
    print(dc)
    if dc:
        dc = UserOrder.objects.get(Product_Id=ProductId,user_email=request.session['useremail'])
        dc.user_order_count - 1
        dc.product_cost - dc.user_order_count
        print(dc.product_cost)
        dc.save()
        db = AddProducts.objects.get(id=ProductId)

        print(db.actualauantity)
        print(db.productquantity)
        if db.productquantity<db.actualauantity:
            print("True")
            db.productquantity = db.productquantity+1
            db.save()
        else:
            messages.warning(request, "You have removed the product and continue shopping")
    else:
        messages.warning(request, "You have removed the product and continue shopping")
    return redirect("allproducts")
    
def newcommunity(request):
    data = Community.objects.all()
    return render(request,communitypage,{'data':data,'email':request.session['useremail']})
    
def community(request):
    dc = User.objects.filter(email=request.session['useremail'])
    for i in dc:
        db = i.username,i.email
    username = db[0]
    email = request.session['useremail']
    # contact = db[2]
    print(username,email)
    status='Joined'
    print(status)
    da = Community(username=username,email=email,status=status)
    da.save()
    request.session['status'] = status
    print(request.session['status'])
    return render(request,communitypage, {'email':request.session['useremail']})
     
from .models import Community  # Import your Community model

def createcommunity(request):
    if request.method == "POST":
        communityname = request.POST['communityname']
        communitydescription = request.POST['communitydescription']
        Communitytype = request.POST['Communitytype']
        today_date = date.today()
        # Create a new instance of the Community model
        new_community = Community.objects.create(
            communityname=communityname,
            communitydescription=communitydescription,
            Communitytype=Communitytype,
            owneremail=request.session['useremail'],
            today_date=today_date
        )
        # Save the instance to the database
        new_community.save()
        messages.success(request, 'New Community Created successfully.')
        return render(request, createcomminitypage, {'email': request.session['useremail']})
    return render(request, createcomminitypage, {'email': request.session['useremail']})
    
def viewcommunity(request):
    data = Community.objects.all()
    return render(request,viewcommunitypage,{'data':data})
   
def Joincommunity(request,id):
    print(id)
    join_community = Community.objects.filter(id = id)
    xc =[ (i.id,i.communityname,i.communitydescription,i.Communitytype,i.owneremail) for i in join_community][0]
    CommunityId = xc[0]
    communityname = xc[1]
    communitydescription = xc[2]
    Communitytype = xc[3]
    owneremail = xc[4]
    useremail = request.session['useremail']
    insert_data = Member.objects.create(
            CommunityId=CommunityId,
            communityname=communityname,
            communitydescription=communitydescription,
            Communitytype=Communitytype,
            owneremail=owneremail,
            email = useremail
        )
    insert_data.save()
    return redirect("viewcommunity")

def viewmember(request):
    data = Member.objects.all()
    return render(request,viememberpage,{'data':data,'email':request.session['useremail']})
    data = RentAmount.objects.filter(useremail=request.session['useremail'])
    print("789789789")
    return render(request,fromrentrequestspage,{'data':data,'email':request.session['useremail']})

def viewcard(request):
    my_products = AddProducts.objects.all()
    print(my_products) 
    my_profile = UserOrder.objects.filter(user_email=request.session['useremail'])
    return render(request,viewmycard,{'my_profile':my_profile,my_products:'my_products','email':request.session['useremail']})