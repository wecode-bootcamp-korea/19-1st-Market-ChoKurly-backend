import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketkurly.settings")
django.setup()

from products.models import *
from orders.models import *
CSV_PATH_PRODUCTS = './test.csv'
with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        # print(row)
        #
        # Category.objects.create(
        #         name = row[0]
        #         )

        # SubCategory.objects.create(
        #         name  =   row[0],
        #         category_id= row[1]
        #         )

        # DiscountRate.objects.create(
        #     discount_rate = row[0]
        # )

        # Sticker.objects.create(
        #     name=row[0]
        # )
        # #
        # Product.objects.create(
        #         name = row[0],
        #         category_id=row[1],
        #         stock=row[2],
        #         price=row[3],
        #         sub_category_id=row[4],
        #         discount_rate_id = row[5],
        #         thumbnail_image=row[6],
        #         description_image=row[7],
        #         size_image=row[8],
        #         sticker_id=row[9]
        #         )
        #
        # Allergy.objects.create(
        #     name=row[0]
        # )

        # ProductInformation.objects.create(
        #         sale_unit = row[0],
        #         weight_g  = row[1],
        #         delivery_type= row[2],
        #         packing_type= row[3],
        #         instruction= row[4],
        #         product_id= row[5],
        #         comment= row[6],
        #        # allergy_id= row[7]
        # )
        #
        # OrderStatus.objects.create(
        #     name = row[0]
        # )

        # PaymentType.objects.create(
        #     name = row[0]
        # )
        #
        ShippingMethod.objects.create(
            name = row[0]
        )


        # #image_url 생성
        # Image.objects.create(
        #         image_url = row[0],
        #         product_id= row[1]
        #         )
