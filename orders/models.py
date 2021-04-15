from django.db import models

class Order(models.Model):
    total_quantity     =   models.IntegerField(default=0)
    shipping_price     =   models.DecimalField(max_digits = 7,decimal_places = 2,null=True)
    user               =   models.ForeignKey('users.User',on_delete = models.CASCADE)
    total_price        =   models.DecimalField(max_digits=10 ,decimal_places = 2,null=True)
    order_status       =   models.ForeignKey('OrderStatus',on_delete = models.SET_NULL ,null=True)
    payment_type       =   models.ForeignKey('PaymentType',on_delete = models.SET_NULL ,null=True)
    shipping_method    =   models.ForeignKey('ShippingMethod',on_delete = models.SET_NULL ,null=True)
    product            =   models.ManyToManyField('products.Product',through='Cart')
    created_at         =   models.DateTimeField(auto_now_add=True)
    updated_at         =   models.DateTimeField(auto_now=True)

    class Meta:
        db_table       =  'orders'

class ShippingMethod(models.Model):
    name               =   models.CharField(max_length=45)
    
    class Meta:
        db_table       =   'shipping_methods'

class OrderStatus(models.Model):
    name              =   models.CharField(max_length=45)

    class Meta:
        db_table     =   'order_status'

class Cart(models.Model):
    product          =   models.ForeignKey('products.Product', on_delete = models.CASCADE)
    order            =   models.ForeignKey('Order', on_delete= models.CASCADE)
    quantity         =   models.IntegerField(default=0)

    class Meta:
        db_table     =  'carts'

class PaymentType(models.Model):
    name             =   models.CharField(max_length=45)

    class Meta:
        db_table     =  'payment_types'
