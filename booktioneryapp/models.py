from django.db import models
from datetime import date, datetime
import re
import bcrypt
class UserManager(models.Manager):
    def basic_validator_register(self, postData):
        errors = {}
        user = User.objects.filter(mobile_number = postData['mobile_number'])
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first name should be at least 2 characters"
        if not postData['first_name'].isalpha():
            errors["first_name"] = "first name should be characters only"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last name should be at least 2 characters"
        if not postData['last_name'].isalpha():
            errors["last_name"] = "last name should be characters only"
        if len(postData['mobile_number']) < 10:
            errors['mobile_number'] = "Invalid Mobile Number address!"
        if len(user):
            errors['mobile_number'] = "Mobile already registered"
        if len(postData['password']) < 8:
            errors["password"] = " password should be at least 8 characters"
        if postData['confirm'] != postData['password']:
            errors["confirm"] = "confirm password should match with password"
        return errors
    def basic_validator_login(self, postData):
        errors = {}
        user = User.objects.filter(mobile_number = postData['mobile_number'])
        if  len(postData['mobile_number']) < 10:
            errors['mobile_number'] = "wrong Mobile Number!"
        if not len(user):
            errors['mobile_number'] = "Wrong Mobile Number Or not registered"
        if len(postData['password']) < 8:
            errors["password"] = "you should enter the password"
        if len(user) and not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
            errors["password"] = "Wrong Password!"
        return errors


class Role(models.Model):
    role_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    address = models.TextField()
    password =  models.CharField(max_length=255)
    role = models.ForeignKey(Role, related_name="role_users",default=2, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    cat= models.ForeignKey(Category, related_name="Category_products", on_delete = models.CASCADE)
    available_quantity = models.IntegerField()
    img = models.CharField(max_length=255)
    #created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Order(models.Model):
    user = models.ForeignKey(User, related_name="user_orders", on_delete = models.CASCADE)
    # product = models.ManyToManyField(Product, related_name="product_orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.FloatField(null=True)



class Cart(models.Model):
    user = models.ForeignKey(User, related_name="user_cart", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_cart", on_delete = models.CASCADE)
    order = models.ForeignKey(Order, related_name="order_cart",null=True, on_delete = models.CASCADE)
    quantity=models.DecimalField(decimal_places=0, max_digits=2)
    deleted = models.DecimalField(decimal_places=0, max_digits=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def reg_errors(check_info):
    errors = User.objects.basic_validator_register(check_info)
    return errors

def login_errors(check_info):
    errors = User.objects.basic_validator_login(check_info)
    return errors


def register(reg_info):
    first_name = reg_info['first_name']
    last_name = reg_info['last_name']
    mobile_no = reg_info['mobile_number']
    password = reg_info['password']
    confirm_password = reg_info['confirm']
    user = User.objects.filter(mobile_number = mobile_no)
    if len(user) == 0:
        if password == confirm_password :
            crypt_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=first_name,last_name=last_name,mobile_number=mobile_no,password=crypt_password)
            user_info = User.objects.last()
            return user_info
    return False


def login(log_info):
    user_in_data = User.objects.filter(mobile_number=log_info['mobile_number'])
    if len(user_in_data):
        if bcrypt.checkpw(log_info['password'].encode(), user_in_data[0].password.encode()):
            return user_in_data[0]
    return False

def get_user(user_id):
    user = User.objects.get(id=user_id)
    return user

def all_users():
    return User.objects.all()

def user_orders(user_id):
    user = User.objects.get(id=user_id)
    orders = user.user_orders.all()
    return orders

def all_products():
    products = Product.objects.all()
    return products



def get_product(product_id):
    product = Product.objects.filter(id=product_id)
    return product[0]

def get_product_by_name(product_name):
    productname = product_name['product']
    product = Product.objects.filter(name=productname)
    return product[0]

def all_categorys():
    category_list = Category.objects.all()
    return category_list

def get_category(product_cat_name):
    category = Category.objects.filter(name=product_cat_name)
    return category[0]

def add_to_cart(user,product):
    Cart.objects.create(user=user,product=product,quantity=1,deleted=0)

def add_to_cart_from_product(data,user_id,product_id):
    quantity=int(data['quantity'])
    user=User.objects.get(id=user_id)
    product=Product.objects.filter(id=product_id)
    Cart.objects.create(user=user,product=product[0],quantity=quantity,deleted=0)

def get_user_cart(user):
    cart_content = user.user_cart.filter(deleted=0)
    return cart_content

def add_order(user_id):
    user=User.objects.get(id=user_id)
    userCart=Cart.objects.filter(user=user,deleted=0)
    if len(userCart)>0:
        Order.objects.create(user=user)
        user.user_orders.add(Order.objects.last())
        lastOrder=Order.objects.last()
    order_total_price=0
    for product in userCart:
        if product.product.available_quantity >0:
            lastOrder.order_cart.add(product)
            order_total_price+=float(product.product.price)*float(product.quantity)
            cartDelete=product
            cartDelete.deleted = 1
            cartDelete.save()
            product.product.available_quantity-=product.quantity
            product.product.save()
    lastOrder.total_price=order_total_price
    lastOrder.save()
    context= {
        'orderItems':lastOrder.order_cart.filter(deleted=1),
        'order_total_price':order_total_price,
    }
    return context


def item_to_delete(item_id):
    item_to_delete = Cart.objects.get(id=item_id)
    item_to_delete.delete()

def all_orders():
    return Order.objects.all()

def adminLogin(log_info):
    user_in_data = User.objects.filter(mobile_number=log_info['mobile_number'])
    if len(user_in_data):
        if user_in_data[0].role.role_name == 'admin':
            if bcrypt.checkpw(log_info['password'].encode(), user_in_data[0].password.encode()):
                return user_in_data[0]
    return False

def delete_product(product_id):
    product = Product.objects.get(id=product_id)
    product.delete()

def update_product(product_info,product_id):
    product=Product.objects.get(id=product_id)
    product.name=product_info['name']
    product.description=product_info['description']
    product.price=product_info['price']
    product.available_quantity=product_info['available_quantity']
    product.cat=Category.objects.get(name=product_info['category'])
    print(product.cat.name)
    product.save()
    return product


# def add_product(product_info):
#     #product=Product.objects.get(id=product_id)
#     product.name=product_info['name']
#     product.description=product_info['description']
#     product.price=product_info['price']
#     product.available_quantity=product_info['available_quantity']
#     product.cat=Category.objects.get(name=product_info['category'])
#     return product

