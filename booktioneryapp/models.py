from django.db import models

class User_Role(models.Model):
    role_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    address = models.TextField()
    password =  models.CharField(max_length=255)
    role = models.ForeignKey(User_Role, related_name="role_users", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    product= models.ForeignKey(Category, related_name="Category_products", on_delete = models.CASCADE)
    available_quantity = models.IntegerField()
    img = models.ImageField()
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
