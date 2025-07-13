from django.db import models

# Create your models here.
#Each fields in the Django will have there compulsary argument/paramter some fields have compulsary to pas such arguments
# Promotion - Product (To learn manytomany fields) promotion can many product and many product can many promotions

class Promotion(models.Model):
    description=models.CharField(max_length=255)
    discount=models.FloatField()
class Collection(models.Model):
    title = models.CharField(max_length=255)
    feature_product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')# we are definig here to avoid the circular depedency create by the product and the circular models ,,
# django will create reverse relation so we can either create  reverse relation or we can define the name by giving int to the related_name and if we pass + in related name it will not create reverse relationship
class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.ImageField()
    last_update=models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions=models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMEBERSHIP_BRONZE='B'
    MEMEBERSHIP_SILVER='S'
    MEMEBERSHIP_GOLD='G'

    MEMEBERSHIP_CHOICES=[
        (MEMEBERSHIP_BRONZE,'Bronze'),
        (MEMEBERSHIP_SILVER,'Silver'),
        (MEMEBERSHIP_GOLD,'Gold'),
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=MEMEBERSHIP_CHOICES,default=MEMEBERSHIP_BRONZE)

class Order(models.Model):
    STATUS_PENDING='P'
    STATUS_COMPLETE='C'
    STATUS_FAILED='F'

    PAYMENT_STATUS=[
        (STATUS_PENDING,'pending'),
        (STATUS_FAILED,'failed'),
        (STATUS_COMPLETE,'complete'),
    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STATUS,default=STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()







