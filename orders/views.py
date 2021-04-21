import json

from .models            import Order, ShippingMethod,OrderStatus,Cart,PaymentType
from users.models       import User
from users.decorators   import login_required

from django.db.models   import Q
from django.http        import JsonResponse
from django.views       import View

class OrderformView(View):
    @login_required
    def get(self, request):
        if Order.objects.filter(Q(user_id = request.user) & Q(order_status_id = 1) | Q(order_status_id = 2)).exists():
            ordercheck   = Order.objects.get(user_id = request.user)  
            user         = User.objects.get(id = request.user)
            
            if ordercheck.total_price > 10000.00:
                ordercheck.shipping_price = None
                ordercheck.save()

            products=[{
                'product_id': product.product.id,
                'product_name': product.product.name,
                'product_quantity': product.quantity,
                'product_thumbnail_image': product.product.thumbnail_image,
                'product_price': int(product.product.price),
                'product_discount_price': int(product.product.price - ( product.product.discount_rate.discount_rate * product.product.price if product.product.discount_rate.discount_rate is not None else None)),
            }for product in ordercheck.cart_set.all()]

            result=[{
                'order_product':products,
                'user_name': user.name,
                'user_phone':user.phone_number,
                'user_email':user.email,
                'user_address': user.address_set.get(is_default=1).address,
                'shipping_price': ordercheck.shipping_price
                } ]

            ordercheck.order_status_id = 2
            ordercheck.save()
            return JsonResponse({'result':result}, status=200)   

        return JsonResponse({'MESSAGE':'Don\'t have anything to order'}, status=400)
