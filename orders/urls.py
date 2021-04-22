from .views         import OrderformView, OrderDetailView, BasketView
from django.urls    import path

urlpatterns=[
        path('/orders',OrderformView.as_view()),
        path('/order-details',OrderformView.as_view()),
        path('/basket', BasketView.as_view()),
        ]
