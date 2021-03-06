from .views         import OrderformView, OrderDetailView, BasketView, BasketAddressView, BasketQuantityView
from django.urls    import path

urlpatterns=[
        path('/orders',OrderformView.as_view()),
        path('/order-details',OrderformView.as_view()),
        path('/basket', BasketView.as_view()),
        path('/basket-address', BasketAddressView.as_view()),
        path('/basket-quantity', BasketQuantityView.as_view())
        ]
