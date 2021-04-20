from django.views    import View
from django.http     import JsonResponse

from products.models import (
    Product, Category,
    SubCategory, Allergy,
    ProductInformation,
    AllergyProduct, Image,
    DiscountRate)

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

        return JsonResponse({'results': results}, status=200)

class ProductView(View):
    def get(self,request):
        section_type  = request.GET.get('section_type', None)
        product_count = int(request.GET.get('product_count', 9))
        products      = Product.objects.order_by(section_type)[:product_count]

        results = [{

            "id": product.id,
            "name": product.name,
            "price": int(product.price),
            "discount_rate": product.discount_rate.discount_rate if product.discount_rate else None,
            "discounted_price": int(product.price - (product.price * product.discount_rate.discount_rate)) if product.discount_rate else None,
            "thumbnail_image": product.thumbnail_image,
            "sticker": product.sticker.name if product.sticker else None

        } for product in products]

        return JsonResponse({'results':results}, status=200)

class ProductFilterView(View):
    def get(self, request):
        category_id     = request.GET.get('category_id',None)
        sub_category_id = request.GET.get('sub_category_id',None)
        order_by_type   = request.GET.get('order_by_type','?')
        product_count   = int(request.GET.get('product_count',9))

        if category_id:
            products = Product.objects.filter(category_id=category_id).order_by(order_by_type)[:product_count]
        if sub_category_id:
            products = Product.objects.filter(sub_category_id=sub_category_id).order_by(order_by_type)[:product_count]

        results = [
            {
                "id": product.id,
                "name": product.name,
                "original_price": int(product.price),
                "discount_rate": float(product.discount_rate.discount_rate) if product.discount_rate else None,
                "discounted_price": int(product.price - (product.price * product.discount_rate.discount_rate)) if product.discount_rate else None,
                "thumbnail_image": product.thumbnail_image,
                "sticker": product.sticker.name if product.sticker else None,
                "comment":product.productinformation.comment if product.productinformation.comment else None
            } for product in products]

        return JsonResponse({'results':results}, status=200)