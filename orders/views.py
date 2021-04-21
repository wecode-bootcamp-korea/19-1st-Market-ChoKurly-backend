import json
import jwt
import my_settings

from .models            import Order, ShippingMethod,OrderStatus,Cart,PaymentType
from users.models       import User, Address
from users.decorators   import login_required
from products.models    import Product

from django.db.models   import Q
from django.http        import JsonResponse
from django.views       import View
from django.db          import transaction

class OrderformView(View):
    @login_required
    def get(self, request):
        if Order.objects.filter(Q(user_id = request.user) & Q(order_status_id = 1) | Q(order_status_id = 2)).exists():
            ordercheck   = Order.objects.get(user_id = request.user)
            
            if ordercheck.total_price > 10000.00:
                ordercheck.shipping_price = None
                ordercheck.save()

            products=[{
                'product_id': product.product.id,
                'product_name': product.product.name,
                'product_quantity': product.quantity,
                'product_thumbnail_image': product.product.thumbnail_image,
                'product_price': int(product.product.price),
                'product_discount_price': int(product.product.price - ( product.product.discount_rate.discount_rate * product.product.price if product.product.discount_rate.discount_rate else None)),
            }for product in ordercheck.cart_set.all()]

            result=[{
                'order_product':products,
                'user_name': request.user.name,
                'user_phone':request.user.phone_number,
                'user_email':request.user.email,
                'user_address': request.user.address_set.get(is_default=1).address,
                'shipping_price': ordercheck.shipping_price
                } ]

            ordercheck.order_status_id = 2
            ordercheck.save()
            return JsonResponse({'result':result}, status=200)   

        return JsonResponse({'MESSAGE':'Don\'t have anything to order'}, status=400)

class BasketView(View):
    @login_required
    def get(self, request):
        try:
            encoded_token = request.headers['Authorization']
            decoded_token = jwt.decode(encoded_token, my_settings.SECRET['secret'], algorithms='HS256')
           
            user_id            = decoded_token['user id']

            if not user_id:
                return JsonResponse({'message':'INVALID_USER_ID'}, status=400)
            
            address                = Address.objects.filter(
                Q(user_id=user_id) & Q(is_default=True)
            )

            if not address:
                return JsonResponse({'message':'UNKOWN_USER'}, status=400)

            order                  = Order.objects.filter(user_id=user_id).first()
            
            if order:
                cart_list          = Cart.objects.filter(order_id=order.id)
                cart_product_info  = [{
                    'id'              : '{}'.format(i+1),
                    'product_id'      : cart_list[i].product.id,
                    'name'            : cart_list[i].product.name,
                    'price'           : cart_list[i].product.price * cart_list[i].quantity,
                    'quantity'        : cart_list[i].quantity,
                    'thumbnail_image' : cart_list[i].product.thumbnail_image
                } for i in range(len(cart_list))]

                result             = [{
                    'id'                   : '1',
                    'user_id'              : user_id,
                    'address'              : address.first().address,
                    'cart_product_info'    : cart_product_info
                }]
            else:
                result             = [{
                    'id'                   : '1',
                    'user_id'              : user_id,
                    'address'              : None,  
                    'cart_product_info'    : None,
                }]

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'message':'JSON_Decode_Error'}, status=400)
        
        return JsonResponse({'result' : result}, status=200)
