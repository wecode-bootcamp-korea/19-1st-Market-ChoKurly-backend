from .views         import OrderformView, BasketView
from django.urls    import path

urlpatterns=[
        path('/orders',OrderformView.as_view()),
        path('/basket', BasketView.as_view()),
        ]
