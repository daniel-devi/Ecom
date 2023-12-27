from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete= models.CASCADE)
    name = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self) :
        return f"{self.name}"
    


class Product(models.Model):
    name = models.CharField(max_length=20,null=True, blank=True)
    description = models.CharField(max_length=20000,null=True, blank=True)
    product_info = models.CharField(max_length=200000,null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads', null=True, blank=True, default='img/placeholder.png')
    digital = models.BooleanField(null=True, blank=True, default=False)
    product_Slug = models.SlugField(blank=True)

    def __str__(self) :
        return f"{self.name}"
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        self.product_Slug = self.id
        super().save(*args, **kwargs)


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete= models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) :
        return f"{self.id}"
    
    @property
    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitem])
        return total

    @property
    def get_cart_items(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitem])
        return total
    
    @property
    def shipping(self):
        shipping = False    
        orderitem = self.orderitem_set.all()
        for i in orderitem:
            if i.product.digital == False:
                shipping = True
        return shipping



class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete= models.SET_NULL)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete= models.SET_NULL)
    quantity =  models.PositiveIntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"{self.product}"
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total




class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete= models.SET_NULL)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete= models.SET_NULL)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) :
        return f"{self.address}"
  