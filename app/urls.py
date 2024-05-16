from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('user',views.user,name="user"),
    path('userreg',views.userreg,name='userreg'),
    path('viewmyprofile',views.viewmyprofile,name='viewmyprofile'),
    path('myproducts',views.myproducts,name="myproducts"),
    path('addproducts',views.addproducts,name="addproducts"),
    path('allproducts',views.allproducts,name="allproducts"),
    path('updateproduct/<int:id>',views.updateproduct,name="updateproduct"),
    path('modifyproduct',views.modifyproduct,name="modifyproduct"),
    path('deleteproduct/<int:id>',views.deleteproduct,name="deleteproduct"),
    path('addproduct/<int:id>',views.addproduct,name="addproduct"),
    path('productsremove/<int:ProductId>',views.productsremove,name="productsremove"),
    path('userrequests/<int:id>',views.userrequests,name="userrequests"),
    path('acceptproduct/<int:Product_Id>/<str:user_email>',views.acceptproduct,name="acceptproduct"),
    path('payment/<int:ProductId>',views.payment,name="payment"),
    path('pay/<int:Product_Id>',views.pay,name="pay"),
    path('allpayment',views.allpayment,name="allpayment"),
    path('viewallpayments/<int:Product_Id>',views.viewallpayments,name="viewallpayments"),
    path('rentamount/<int:Product_Id>',views.rentamount,name="rentamount"),
    path('myrentrequests',views.myrentrequests,name="myrentrequests"),
    path('newaccept/<int:ProductId>',views.newaccept,name="newaccept"),
    path('Cashonpayment/<int:ProductId>',views.Cashonpayment,name="Cashonpayment"),
    path('exchange/<int:ProductId>',views.exchange,name="exchange"),
    path('searchproduct',views.searchproduct,name="searchproduct"),
    path('newcommunity',views.newcommunity,name="newcommunity"),
    path('createcommunity',views.createcommunity,name="createcommunity"),
    path('viewcommunity',views.viewcommunity,name="viewcommunity"),
    path('Joincommunity/<int:id>',views.Joincommunity,name="Joincommunity"),
    path('viewmember',views.viewmember,name="viewmember"),
    path('myproductsmore/<int:id>',views.myproductsmore,name="myproductsmore"),
    path('allproductsmore/<int:id>',views.allproductsmore,name="allproductsmore"),
    path('viewcard',views.viewcard,name="viewcard"),
    path('allproductshome',views.allproductshome,name="allproductshome"),
    path('searchproduct1',views.searchproduct1,name="searchproduct1"),


    
]