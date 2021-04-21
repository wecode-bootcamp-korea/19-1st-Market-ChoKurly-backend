import json
import random

from django.views    import View
from django.http     import JsonResponse

from products.models import (
    Product, Category,
    SubCategory, Allergy,
    ProductInformation,
    AllergyProduct, DiscountRate)

class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()

        RESULTS = [
            {
                'id'          : category.id,
                'category'    : category.name,
                'sub_category': [{
                    'id'  : subcategory.id,
                    'name': subcategory.name
                } for subcategory in category.subcategory_set.all()]
            } for category in categories]

        return JsonResponse({'RESULTS': RESULTS}, status=200)

class ProductListView(View):
    def get(self,request):
        category_id     = request.GET.get('category_id', None)
        sub_category_id = request.GET.get('sub_category_id', None)
        order_by_type   = request.GET.get('order_by_type', None)
        page            = int(request.GET.get('page', 1))
        limit           = int(request.GET.get('limit', 8))
        start           = (page - 1) * limit
        end             = page * limit

        if not category_id and not sub_category_id:
            products = Product.objects.order_by(order_by_type)[start:end]
        if category_id:
            products = Product.objects.filter(category_id=category_id).order_by(order_by_type)[start:end]
        if sub_category_id:
            products = Product.objects.filter(sub_category_id=sub_category_id).order_by(order_by_type)[start:end]

        RESULTS = [{

            "id": product.id,
            "name": product.name,
            "original_price": int(product.price),
            "discount_rate": float(product.discount_rate.discount_rate) if product.discount_rate else None,
            "discounted_price": int(product.price - (product.price * product.discount_rate.discount_rate)) if product.discount_rate else None,
            "thumbnail_image": product.thumbnail_image,
            "sticker": product.sticker.name if product.sticker else None,
            "comment": product.productinformation.comment if category_id or sub_category_id else None

        } for product in products]

<<<<<<< HEAD
        return JsonResponse({'results':results}, status=200)

class ProductDetailView(View):
    def get(self, request, product_id):
        product                 = Product.objects.get(id=product_id)
        product_info            = product.productinformation
        allergy_info            = AllergyProduct.objects.filter(
            product_information=product_info.id
        )
        
        allergy_list            = [{
            'id'      : '{}'.format(index+1),
            'allergy' : allergy_info[index].allergy.name
        } for index in range(len(allergy_info))]

        picked_related_products = self.pick_related_product([
            related_product for related_product in Product.objects.all()
        ])
        
        related_product_list    = self.make_related_product_list(picked_related_products) 
#
        result                  = [{
            'id'                : "1",
            'discount_rate'     : float(product.discount_rate.discount_rate), # 할인율
            'name'              : product.name,                               # 상품명
            'comment'           : product_info.comment,                       # 상품 코멘트
            'price'             : int(product.price),                         # 상품가격
            'sale_unit'         : product_info.sale_unit,                     # 판매단위
            'weight_g'          : float(product_info.weight_g),               # 중량/용량
            'delivery_type'     : product_info.delivery_type,                 # 배송구분
            'packing_type'      : product_info.packing_type,                  # 포장타입
            'allergy'           : allergy_list,                               # 알레르기 정보
            'instruction'       : product_info.instruction,                   # 안내사항
            'review'            : None,                                       # 상품 리뷰
            'thumbnail_image'   : product.thumbnail_image,                    # 상품 섬네일 이미지
            'description_image' : product.description_image,                  # 상품 description_image
            'size_image'        : product.size_image,                         # 상품 size_image
            'related_products'  : related_product_list,                       # 관련 상품
            }]
        
        return JsonResponse({'result' : result}, status=200)

    def pick_related_product(self, info):
        random.shuffle(info)
        result = [info[index] for index in range(10)]
        return result

    def make_related_product_list(self, picked_related_products):
        result           = [{
            'id' : '{}'.format(index+1),
            'name' : picked_related_products[index].name,
            'price': int(picked_related_products[index].price),
            'rel_img': picked_related_products[index].thumbnail_image,
        } for index in range(len(picked_related_products))]
        return result
=======
        return JsonResponse({'RESULTS':RESULTS}, status=200)
>>>>>>> main
