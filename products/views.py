from django.views    import View
from django.http     import JsonResponse

from products.models import Product, Category, SubCategory, Allergy, ProductInformation, AllergyProduct, Image, DiscountRate

class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        results = []
        for category in categories:
            sub_categories = SubCategory.objects.filter(category_id=category.id)
            sub_category_lists = []
            for sub_category in sub_categories:
                sub_category_lists.append(
                    {
                    'id':sub_category.id,
                    'name':sub_category.name
                    }
                )
            results.append(
                {
                    'id' : category.id,
                    'category': category.name,
                    'sub_category': sub_category_lists

                }
            )
        return JsonResponse({'results':results}, status=200)