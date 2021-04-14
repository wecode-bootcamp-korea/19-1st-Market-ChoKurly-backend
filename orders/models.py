from django.db import models

class Order(models.Model):
    total_quantity     =   models.IntegerField(null=True)
    shipping_price     =   models.DecimalField(max_digits=7,decimal_places=2,null=True)
    user               =   models.ForeignKey('users.User',on_delete = models.CASCADE)
    total_price        =   models.DecimalField(max_digits=10,decimal_places=2,null=True)
    status             =   models.ForeignKey('OrderStatus',on_delete = models.CASCADE)
    payment_type       =   models.ForeignKey('PaymentType',on_delete = models.CASCADE,null=True)
    shipping_method    =   models.CharField(max_length=45,null=True)
    product            =   models.ManyToManyField('products.Product',through='Cart')
    created_at         =   models.DateTimeField(auto_now_add=True)
    updated_at         =   models.DateTimeField(auto_now=True)

    class Meta:
        db_table     =  'orders'

class OrderStatus(models.Model):
    name             =   models.CharField(max_length=45)

    class Meta:
        db_table     =   'orderstatus'

class Cart(models.Model):
    product          =   models.ForeignKey('products.Product', on_delete = models.CASCADE)
    order            =   models.ForeignKey('Order', on_delete= models.CASCADE)
    quantity         =   models.IntegerField()

    class Meta:
        db_table     =  'carts'

class PaymentType(models.Model):
    name             =   models.CharField(max_length=45)

    class Meta:
        db_table     =  'paymenttypes'
