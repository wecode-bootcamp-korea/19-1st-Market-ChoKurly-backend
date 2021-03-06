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

        results = [
            {
                'id'          : category.id,
                'category'    : category.name,
                'sub_category': [{
                    'id'  : subcategory.id,
                    'name': subcategory.name
                } for subcategory in category.subcategory_set.all()]
            } for category in categories]

        return JsonResponse({'RESULTS': results}, status=200)

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

        results = [{

            "id": product.id,
            "name": product.name,
            "original_price": int(product.price),
            "discount_rate": float(product.discount_rate.discount_rate) if product.discount_rate else None,
            "discounted_price": int(product.price - (product.price * product.discount_rate.discount_rate)) if product.discount_rate else None,
            "thumbnail_image": product.thumbnail_image,
            "sticker": product.sticker.name if product.sticker else None,
            "comment": product.productinformation.comment if category_id or sub_category_id else None

        } for product in products]

        return JsonResponse({'RESULTS':results}, status=200)


class ProductDetailView(View):
    def get(self, request, product_id=None):
        if not product_id:
            return JsonResponse({'message':'ENTER product_id'}, status=400)

        product                 = Product.objects.filter(id=product_id).first()

        if not product:
            return JsonResponse({'message':'UNKNOWN_PRODUCT'}, status=400)
        
        product_info            = product.productinformation

        allergy_list            = [{
            'id'        : '{}'.format(index+1),
            'allergy_id': product_info.allergy.all()[index].id,
            'allergy'   : product_info.allergy.all()[index].name, 
        } for index in range(len(product_info.allergy.all()))]

        picked_related_products = self.pick_related_product([
            related_product for related_product in Product.objects.all()
        ])
        
        related_product_list    = self.make_related_product_list(picked_related_products) 
#
        result                  = [{
            'id'                : "1",
            'product_id'        : product.id,
            'discount_rate'     : float(product.discount_rate.discount_rate), # ?????????
            'name'              : product.name,                               # ?????????
            'comment'           : product_info.comment,                       # ?????? ?????????
            'price'             : int(product.price),                         # ????????????
            'sale_unit'         : product_info.sale_unit,                     # ????????????
            'weight_g'          : float(product_info.weight_g),               # ??????/??????
            'delivery_type'     : product_info.delivery_type,                 # ????????????
            'packing_type'      : product_info.packing_type,                  # ????????????
            'allergy'           : allergy_list,                               # ???????????? ??????
            'instruction'       : product_info.instruction,                   # ????????????
            'review'            : None,                                       # ?????? ??????
            'thumbnail_image'   : product.thumbnail_image,                    # ?????? ????????? ?????????
            'description_image' : product.description_image,                  # ?????? description_image
            'size_image'        : product.size_image,                         # ?????? size_image
            'related_products'  : related_product_list,                       # ?????? ??????
            }]

        return JsonResponse({'result':result}, status=200)

    def pick_related_product(self, info):
        random.shuffle(info)
        result = [info[index] for index in range(10)]
        return result

    def make_related_product_list(self, picked_related_products):
        result           = [{
            'id'         : '{}'.format(index+1),
            'product_id' : picked_related_products[index].id,
            'name'       : picked_related_products[index].name,
            'price'      : int(picked_related_products[index].price),
            'rel_img'    : picked_related_products[index].thumbnail_image,
        } for index in range(len(picked_related_products))]
        return result

class SearchView(View):
    def get(self,request):
        search_content = request.GET.get('search_content',None)

        if not search_content:
            return JsonResponse({'MESSAGE':'INVALID_CONTENT'}, status=400)

        products = Product.objects.filter(name__icontains=search_content)

        results = [
            {
                "id": product.id,
                "name": product.name,
                "original_price": int(product.price),
                "discount_rate": float(product.discount_rate.discount_rate) if product.discount_rate else None,
                "discounted_price": int(product.price - (product.price * product.discount_rate.discount_rate)) if product.discount_rate else None,
                "thumbnail_image": product.thumbnail_image,
                "sticker": product.sticker.name if product.sticker else None,
                "comment":product.productinformation.comment

            } for product in products]

        return JsonResponse({'RESULTS':results}, status=200)



