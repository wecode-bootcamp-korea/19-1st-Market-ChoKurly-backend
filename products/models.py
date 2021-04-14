from django.db import models

class Product(models.Model):
    name            =   models.CharField(max_length=45)
    subcategory     =   models.ForeignKey('SubCategory', on_delete = models.SET_NULL, null=True)
    stock           =   models.PositiveIntegerField()
    price           =   models.DecimalField(max_digits=10, decimal_places=2)
    discount_rate   =   models.OneToOneField('DiscountRate', on_delete = models.SET_NULL, null=True)
    category        =   models.ForeignKey('Category', on_delete = models.SET_NULL, null=True)
    created_at      =   models.DateTimeField(auto_now_add=True)
    updated_at      =   models.DateTimeField(auto_now=True)

    class Meta:
        db_table    = 'products'

class Category(models.Model):
    name            =   models.CharField(max_length=45)

    class Meta:
        db_table    = 'categories'

class SubCategory(models.Model):
    name            = models.CharField(max_length=45)
    category        = models.ForeignKey('Category', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table    = 'subcategories'

class Allergy(models.Model):
    name            = models.CharField(max_length=45)

    class Meta:
        db_table    = 'allergies'

class ProductInformation(models.Model):
    sale_unit       =  models.CharField(max_length=45)
    weight_g        =  models.DecimalField(max_digits=3, decimal_places=2)
    delivery_type   =  models.CharField(max_length=45)
    packing_type    =  models.CharField(max_length=45)
    instruction     =  models.TextField(null=True)
    product         =  models.OneToOneField('Product' ,on_delete = models.CASCADE)
    comment         =  models.CharField(max_length=100,null=True)
    allergy         =  models.ManyToManyField('Allergy', through = 'AllergyProduct')

    class Meta:
        db_table = 'productinformations'

class AllegyProduct(models.Model):
    allergy             = models.ForeignKey('Allergy', on_delete = models.CASCADE)
    productinformation  = models.ForeignKey('ProductInformation', on_delete = models.CASCADE)

    class Meta:
        db_table = 'allegyproducts'

class Image(models.Model):
    image_url       = models.URLField(max_length=2000)
    product         = models.ForeignKey('Product',on_delete = models.CASCADE)

    class Meta:
        db_table    = 'images'

class DiscountRate(models.Model):
    discount_rate   = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table    = 'discountrates'

