from .views         import OrderformView, OrderDetailView
from django.urls    import path

urlpatterns=[
        path('/orders',OrderformView.as_view()),
        path('/order-details',OrderformView.as_view()),
        ]
