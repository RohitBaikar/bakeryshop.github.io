import json
from django.shortcuts import render,redirect
from . forms import RegisterForm,LoginForm , ContactForm , CategoryForm,ProductForm
from django.contrib.auth import authenticate,login,logout
from . models import CategoryModel,Products,ContactUs , Cart ,Register
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home_view(request):
    categories=CategoryModel.objects.all()
    Images=Products.objects.all()
    current_user = request.user
    userid=current_user.id
    
    print(userid)
    context={"categories":categories, 'Images':Images,'userid':userid}

    return render(request,'BakeryApp/home.html', context)

def signup_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        address=request.POST['address']
        contact=request.POST['contact']
        
        password=request.POST['password2']
        
        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)

        Register.objects.create(user=user,address=address,contact=contact)
        # form = RegisterForm(request.POST)
        # if form.is_valid():
        # Pro.save()
        messages.success(request,'Successfully Created Account..')
        return redirect('home')
    # context = {'Register':Register}
    
    return render(request,'BakeryApp/signup.html')

def signout_view(request):
    logout(request)
    messages.success(request, "Successfully logout...")
    return redirect('home')

def signin_view(request):
    form = LoginForm()
    context = {'form':form}   
    if request.method == 'POST':
        username = request.POST["username"]
        pass1 = request.POST["password"]
        user = authenticate(username = username, password = pass1)
        
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully USER LOG IN...')
            return redirect('home')
        else:
            messages.warning(request,'Can Not Find USER')
            return redirect('signin')

    return render(request,'BakeryApp/signin.html',context)


def catimage_view(request, id):
    # print('id is ',id)
    categories=CategoryModel.objects.all()
    cat=CategoryModel.objects.get(id=id)
    Images=Products.objects.filter(cat= cat)
    context={'categories':categories,'Images':Images}
    return render(request, 'BakeryApp/home.html', context)


def image_view(request, id):
    image = Products.objects.get(id = id)
    print('id is ',id)
    context = {'image':image}
    return render(request,'BakeryApp/products.html',context)
   
def adminsignin_view(request):
    form = LoginForm()
    context = {'form':form}   

    if request.method == 'POST':
        username = request.POST["username"]
        pass1 = request.POST["password"]

        user = authenticate(username = username, password = pass1)

        if user is not None:
            if user.is_staff:
                login(request,user)
                messages.success(request,'Successfully Admin LOG IN')
                return redirect('admindashboard')

            else:
                messages.warning(request,'Fill correct admin info..')

        else:
            messages.warning(request,'Something Went Wrong')
            return redirect('adminsignin')

    return render(request,'BakeryApp/adminloginpage.html',context)
    
def adminloginpage_view(request):
    form = LoginForm()
    context = {'form':form}
    return render(request,'BakeryApp/adminloginpage.html',context)

def adminlogout_view(request):
    logout(request)
    messages.success(request, "Successfully Admin logout...")
    return redirect('home')

def contactus_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank You ')
            return redirect('home')
    context = {'form':form}
    return render(request,'BakeryApp/contactus.html',context)


def addcategory_view(request):
    forms = CategoryForm()
    context = {'forms': forms}
  
    if request.method=='POST':
        new_title=request.POST['title']
        Cat=CategoryModel(title=new_title)
        Cat.save()
        messages.success(request,'Successfully Category Added')
        return redirect('addcategory')
    return render(request,'BakeryApp/addcategory.html',context)

def addproduct_view(request):
    forms = ProductForm()
    # context = {'forms': forms}
  
    if request.method=='POST':
        forms = ProductForm(request.POST,request.FILES)

        # img_title=request.POST['img_title']
        # details=request.POST['details']
        # image=request.POST['image']
        # price=request.POST['price']
        # cat=request.POST['cat']
        # Qua=request.POST['Qua']
        # Pro=Products(img_title=img_title,details=details,image=image,price=price,cat=cat,Qua=Qua)
        if forms.is_valid():
            forms.save()
            messages.success(request,'Successfully Product Added')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('addproduct')
        # return redirect('home')
    context = {'forms': forms}
    return render(request,'BakeryApp/addproduct.html',context)


def admindashboard_view(request):
    return render(request,'BakeryApp/admindashboard.html')


def allcategory_view(request):
    categories=CategoryModel.objects.all()
    context = {'categories':categories}
    return render(request,'BakeryApp/allcategory.html',context)

def allproducts_view(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request,'BakeryApp/allproducts.html',context)

def editcategory_view(request,id):
    category = CategoryModel.objects.get(id=id)
    context = {'category':category}
    if request.method =='POST':
        name = request.POST['name']
        category.title = name
        category.save()
        messages.success(request,'Successfully Update Category')
        return redirect('allcategory')
    
    return render(request,'BakeryApp/editcategory.html',context)

    
def deletecategory_view(request,id):
    category = CategoryModel.objects.get(id=id)
    category.delete()
    return redirect('allcategory')


def editproduct_view(request,id):
    product = Products.objects.get(id=id)
    category = CategoryModel.objects.all()
    context ={'product':product,'category':category}

    if request.method == 'POST':
        name = request.POST['name']
        details = request.POST['details']
        image = request.FILES['image']
        price = request.POST['price']
        cat = request.POST['category']
        # catobj = CategoryModel.objects.get(id=cat)
        Qua = request.POST['Qua']

        product.img_title = name
        product.details = details
        product.image = image
        product.price = price
        # product.cat = catobj
        product.Qua = Qua

        product.save()
        messages.success(request,'Successfully Update Product')
        return redirect('allproducts')

    return render(request,'BakeryApp/editproduct.html',context)

def deleteproduct_view(request,id):
    products = Products.objects.get(id=id)
    products.delete()
    messages.success(request,'Product Successfully Deleted..')
    return redirect('allcategory')

def myprofile(request):
    data = Register.objects.get(user=request.user)
    # prof=Register.objects.filter(user=request.user)
    context={'data':data}
    return render(request,'BakeryApp/myprofile.html',context)
    
# def updateprof(request):
#     return render(request,'BakeryApp/updateprof.html')


def cart(request):
    try:
            
        cart = Cart.objects.get(user=request.user)
        Product = (cart.product).replace("'",'"')
        myli = json.loads(str(Product))
        Product=myli['objects'][0]
    except:    
        Product = []

    lengthpro = len(Product)
    context = {'lengthpro':lengthpro}

    return render(request,'BakeryApp/cart.html',context)

def addToCart(request, pid):
    myli = {"objects":[]}
    try:
        cart = Cart.objects.get(user=request.user)
        myli = json.loads((str(cart.product)).replace("'", '"'))
        try:
            myli['objects'][0][str(pid)] = myli['objects'][0].get(str(pid), 0) + 1
        except:
            myli['objects'].append({str(pid):1})
        cart.product = myli
        cart.save()
    except:
        myli['objects'].append({str(pid): 1})
        cart = Cart.objects.create(user=request.user, product=myli)
    return redirect('cart')

def incredecre(request, pid):
    cart = Cart.objects.get(user=request.user)
    if request.GET.get('action') == "incre":
        myli = json.loads((str(cart.product)).replace("'", '"'))
        myli['objects'][0][str(pid)] = myli['objects'][0].get(str(pid), 0) + 1
    if request.GET.get('action') == "decre":
        myli = json.loads((str(cart.product)).replace("'", '"'))
        if myli['objects'][0][str(pid)] == 1:
            del myli['objects'][0][str(pid)]
        else:
            myli['objects'][0][str(pid)] = myli['objects'][0].get(str(pid), 0) - 1
    cart.product = myli
    cart.save()
    return redirect('cart')

def deletecart(request, pid):
    cart = Cart.objects.get(user=request.user)
    product = (cart.product).replace("'", '"')
    myli = json.loads(str(product))
    del myli['objects'][0][str(pid)]
    cart.product = myli
    cart.save()
    messages.success(request, "Delete Successfully")
    return redirect('cart')