from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_view,name='home'),
    path('signup/',views.signup_view,name='signup'),
    path('signin/',views.signin_view,name='signin'),
    path('logout/',views.signout_view,name='logout'),
    path('catimage/<int:id>', views.catimage_view,name='catimage'),
    path('image/<int:id>', views.image_view,name='image'),
    path('contactus/',views.contactus_view,name='contactus'),
    path('adminsignin/',views.adminsignin_view,name='adminsignin'),
    path('adminlogout/',views.adminlogout_view,name='adminlogout'),
    path('adminloginpage/',views.adminloginpage_view,name='adminlogin'),
    path('addcategory/',views.addcategory_view,name='addcategory'),
    path('addproduct/',views.addproduct_view,name='addproduct'),
    path('admindashboard/',views.admindashboard_view,name='admindashboard'),
    path('allcategory/',views.allcategory_view,name='allcategory'),
    path('addproducts/',views.allproducts_view,name='allproducts'),
    path('editcategory/<int:id>',views.editcategory_view,name='editcategory'),
    path('deletecategory/<int:id>',views.deletecategory_view,name='deletecategory'),
    path('editproduct/<int:id>',views.editproduct_view,name='editproduct'),
    path('deleteproduct/<int:id>',views.deleteproduct_view,name='deleteproduct'),
    path('myprofile/',views.myprofile,name='myprofile'),
    # path('updateprof/',views.updateprof,name='updateprof'),
    path('add-to-cart/<int:pid>/',views.addToCart, name="addToCart"),
    path('cart/',views.cart, name="cart"),
    path('incredecre/<int:pid>/', views.incredecre, name="incredecre"),
    path('deletecart/<int:pid>/', views.deletecart, name="deletecart"),
        

    



]