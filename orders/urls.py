from .views         import OrderformView, OrderDetailView, BasketView, BasketAddressView
from django.urls    import path

urlpatterns=[
        path('/orders',OrderformView.as_view()),
        path('/order-details',OrderformView.as_view()),
        path('/basket', BasketView.as_view()),
        path('/basket-address', BasketAddressView.as_view()),
        ]
