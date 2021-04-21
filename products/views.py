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
        product_count = int(request.GET.get('product_count', 7))
        products      = Product.objects.order_by(section_type)[:product_count]

        RESULTS = [{

            "id": product.id,
            "name": product.name,
            "price": int(product.price),
            "discount_rate": product.discount_rate.discount_rate if product.discount_rate else None,
            "discounted_price": int(product.price - (product.price * product.discount_rate.discount_rate)) if product.discount_rate else None,
            "thumbnail_image": product.thumbnail_image,
            "sticker": product.sticker.name if product.sticker else None

        } for product in products]

        return JsonResponse({'RESULTS':RESULTS}, status=200)
