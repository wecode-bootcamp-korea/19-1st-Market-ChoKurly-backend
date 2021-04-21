from django.db import models

class User(models.Model):
    identification      =   models.CharField(max_length=45)
    password            =   models.CharField(max_length=500)
    name                =   models.CharField(max_length=45)
    email               =   models.CharField(max_length=100)
    phone_number        =   models.CharField(max_length=45)
    birthdate           =   models.CharField(max_length=45)
    gender              =   models.CharField(max_length=10)
    product             =   models.ManyToManyField('products.Product',through = 'UserLike')
    created_at          =   models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table    = 'users'

class Address(models.Model):
    address             =   models.CharField(max_length=500)
    user                =   models.ForeignKey('User',on_delete = models.CASCADE)
    is_default          =   models.BooleanField(default = False)

    class Meta:
        db_table    = 'addresses'

class Review(models.Model):
    user                =   models.ForeignKey('User', on_delete = models.CASCADE)
    review              =   models.TextField()
    order               =   models.ForeignKey('orders.Order', on_delete = models.SET_NULL ,null=True)
    product             =   models.ForeignKey('products.Product', on_delete = models.CASCADE)
    created_at          =   models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table    =  'reviews'

class UserLike(models.Model):
    user                = models.ForeignKey('User', on_delete = models.CASCADE)
    product             = models.ForeignKey('products.Product', on_delete = models.CASCADE)

    class Meta:
        db_table    =   'user_likes'

class Comment(models.Model):
    review              = models.ForeignKey('Review', on_delete = models.CASCADE)
    content             = models.TextField()
    user                = models.ForeignKey('User', on_delete = models.CASCADE)
    created_at          = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table    = 'comments'