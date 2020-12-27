from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from booktioneryapp.models import User,Product,Cart,Category
from . import models
import json
from django.http import JsonResponse


def root(request):
    if 'user_id' in request.session:
        return redirect('/success')
    return render(request,'main.html')

    
def reg(request):
    return render(request,'register.html')

def welcome(request):
    if 'term' in request.GET:
        qs = Product.objects.filter(name__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.name)
        return JsonResponse(titles, safe=False)
    if 'user_id' in request.session:
        return redirect('/success')
    else:
        product_list = models.all_products()
        category_list = models.all_categorys()
        page = request.GET.get('page', 1)
        paginator = Paginator(product_list, 8)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context={
            'products':products,
            'categorys':category_list,
        }
        return render(request,'main.html',context)


def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        product_list = models.all_products()
        category_list = models.all_categorys()
        page = request.GET.get('page', 1)
        paginator = Paginator(product_list, 8)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context={
        'user_id':request.session['user_id'],
        'first_name':request.session['first_name'],
        'last_name':request.session['last_name'],
        'user_id':request.session['user_id'],
        'categorys':category_list,
        'products':products,
        'pos':'main',
        }
        return render(request,'main.html',context)

def category_products(request,category_name):
    category_list = models.all_categorys()
    category = models.get_category(category_name)
    page = request.GET.get('page', 1)
    paginator = Paginator(category.Category_products.all(), 8)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context={
        'products':products,
        'categorys':category_list,
    }
    return render(request,'main.html',context)

def success_category_products(request,category_name):
    if 'user_id' in request.session:
        category_list = models.all_categorys()
        category = models.get_category(category_name)
        page = request.GET.get('page', 1)
        paginator = Paginator(category.Category_products.all(), 8)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    context={
        'first_name':request.session['first_name'],
        'last_name':request.session['last_name'],
        'user_id':request.session['user_id'],
        'categorys':category_list,
        'products':products,
        'pos':'main',
        }
    return render(request,'main.html',context)

def registration(request):
    if request.method =='POST':
        errors = models.reg_errors(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = models.register(request.POST)
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                return redirect('/success')
        return redirect('/')


def login(request):
    if request.method=='POST':
        errors = models.login_errors(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = models.login(request.POST)
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                return redirect('/success')
    return redirect('/')

def user_profile(request,id):
    category_list = models.all_categorys()
    user_orders = models.user_orders(id)
    if 'user_id' in request.session:
        context = {
            'first_name':request.session['first_name'],
            'last_name':request.session['last_name'],
            'user_id':request.session['user_id'],
            'categorys':category_list,
            'user_orders':user_orders,
            'pos':'my_profile',
        }
        return render(request,'user.html',context)



def view_product(request,product_cat_name,product_id):
    product = models.get_product(product_id)
    category = models.get_category(product_cat_name)
    category_list = models.all_categorys()
    print("&"*30)
    print(product.img)
    if 'user_id' in request.session:
        context = {
            'first_name':request.session['first_name'],
            'last_name':request.session['last_name'],
            'user_id':request.session['user_id'],
            'categorys':category_list,
            'pos':'product_page',
            'product':product,
            'category':category.Category_products.all()[0:4],
        }
        return render(request,'product.html',context)
    else:
        context = {
            'categorys':category_list,
            'pos':'product_page',
            'product':product,
            'category':category.Category_products.order_by('-id')[0:4],
        }
        return render(request,'product.html',context)
    return render(request,'product.html',context)


def addcart(request,product_cat_name,productid):
    if 'user_id' in request.session:
        user_adding_product=models.get_user(request.session['user_id'])
        product_to_add=models.get_product(productid)
        if 'cart' not in request.session:
            request.session['cart']=0
        models.add_to_cart(user_adding_product,product_to_add)
        request.session['cart']+=1
        return redirect('/success')


def viewcart(request,userid):
    if 'user_id' in request.session:
        cart_user=models.get_user(userid)
        category_list = models.all_categorys()
        context={
            'cart_content':models.get_user_cart(cart_user),
            'categorys':category_list,
            'user_id':userid,
        }
        print(context)
    return render(request,"cart.html",context)

def addcart2(request,product_id):
    if 'user_id' in request.session:
        if request.method =='POST':
            models.add_to_cart_from_product(request.POST,request.session['user_id'],product_id)
            request.session['cart']+=1
        return redirect('/success')


def order(request,userid):
    if 'cart' in request.session and request.session['cart']>0:
        if 'user_id' in request.session:
            category_list = models.all_categorys()
            order_info = models.add_order(userid)
            context={
                'orderItems':order_info['orderItems'],
                'order_total_price':order_info['order_total_price'],
                'categorys':category_list,
                'pos':'thankyou',
                'user_id':request.session['user_id'],
            }
            request.session['cart'] = 0
        return render(request,'thankyou.html',context)
    else:
        return render(request,"cart.html",context)

def delete_from_cart(request,item_id,user_id):
    models.item_to_delete(item_id)
    request.session['cart']-=1
    return redirect(f'/cart/{user_id}')

def adminlogin(request):
    if 'user_id' in request.session:
        user=models.get_user(request.session['user_id'])
        if user.role.role_name == 'admin':
            return redirect('/admindashboard/orders')
        else:
            return redirect('/success')
    return render(request,"login.html")



def admin(request):
    if request.method=='POST':
        errors = models.login_errors(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/admin')
        else:
            user = models.adminLogin(request.POST)
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                return redirect('/admindashboard/orders')
    return redirect('/admin')
    

def dashboard(request):
    user=models.get_user(request.session['user_id'])
    if user.role.role_name == 'admin':
        context={
            "orders":models.all_orders(),
            'first_name':request.session['first_name'],
        }
        return render(request,"admindashboard.html",context)
    return redirect('/success')

def dashboard_users(request):
    user=models.get_user(request.session['user_id'])
    if user.role.role_name == 'admin':
        context={
            "all_users":models.all_users(),
            'first_name':request.session['first_name'],
        }
        return render(request,"admin_users.html",context)
    return redirect('/success')

def dashboard_products(request):
    user=models.get_user(request.session['user_id'])
    if user.role.role_name == 'admin':
        context={
            "all_products":models.all_products(),
            'first_name':request.session['first_name'],
        }
        return render(request,"admin_products.html",context)
    return redirect('/success')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['first_name']
        del request.session['last_name']
    return redirect('/')

def delete_product(request,product_id):
    models.delete_product(product_id)
    return redirect('/admindashboard/products')

def update_product(request,product_id):
    product=models.get_product(product_id)
    context={
        'product':product,
        'category_list' : models.all_categorys(),
    }
    return render(request,"update_product.html",context)

def update_product2(request,product_id):
    product=models.update_product(request.POST,product_id)
    print(product.cat.name)
    if product:
        return redirect('/admindashboard/products')
    return redirect('/admindashboard/products')


def add_product(request):
    context={
        
        'category_list' : models.all_categorys(),
    }
    return render(request,"add_product.html",context)

def add_product2(request):
    #product=Product.objects.get(id=product_id)
    image=request.POST['image']
    name=request.POST['name']
    description=request.POST['description']
    price=request.POST['price']
    available_quantity=request.POST['available_quantity']
    cat=Category.objects.get(name=request.POST['category'])
    Product.objects.create(name=name,description=description,price=price,cat=cat,available_quantity=available_quantity,img=image)
    return redirect('/admindashboard/products')

def search(request):
    product = models.get_product_by_name(request.POST)
    if product is not None:
        return redirect('/details/'+ product.cat.name +'/'+str(product.id))
    else:
        return redirect('/')