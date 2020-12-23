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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Order(models.Model):
    quantity = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="user_orders", on_delete = models.CASCADE)
    product = models.ManyToManyField(Product, related_name="product_orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Cart(models.Model):
    user = models.ForeignKey(User, related_name="user_cart", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_cart", on_delete = models.CASCADE)
    order = models.ForeignKey(Order, related_name="order_cart", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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

def reg_errors(check_info):
    errors = User.objects.basic_validator_register(check_info)
    return errors

def login_errors(check_info):
    errors = User.objects.basic_validator_login(check_info)
    return errors

