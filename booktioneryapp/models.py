from django.db import models

class User_Role(models.Model):
    role_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
<<<<<<< HEAD
    address = models.TextField()
    password =  models.CharField(max_length=255)
    role = models.ForeignKey(User_Role, related_name="role_users", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


=======
    address = models.CharField(max_length=255)
    password =  models.CharField(max_length=255)
    role_id = models.ForeignKey(User_Role, related_name="user_id", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

>>>>>>> 12b556b72a7873520cd0b60fc3ce4e8f8a1c6b0c
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
<<<<<<< HEAD
    product= models.ForeignKey(Category, related_name="Category_products", on_delete = models.CASCADE)
=======
>>>>>>> 12b556b72a7873520cd0b60fc3ce4e8f8a1c6b0c
    available_quantity = models.IntegerField()
    img = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
<<<<<<< HEAD
    

class Order(models.Model):
    quantity = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="user_orders", on_delete = models.CASCADE)
    product = models.ManyToManyField(Product, related_name="product_orders")
=======

class Order(models.Model):
    quantity = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, related_name="order_id", on_delete = models.CASCADE)
    product_id = models.ManyToManyField(Product, related_name="order_id")
>>>>>>> 12b556b72a7873520cd0b60fc3ce4e8f8a1c6b0c
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


<<<<<<< HEAD

class Cart(models.Model):
    user = models.ForeignKey(User, related_name="user_cart", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_cart", on_delete = models.CASCADE)
    order = models.ForeignKey(Order, related_name="order_cart", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
=======
class Category(models.Model):
    name = models.CharField(max_length=255)
    product_id = models.ForeignKey(Product, related_name="category_id", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




>>>>>>> 12b556b72a7873520cd0b60fc3ce4e8f8a1c6b0c
