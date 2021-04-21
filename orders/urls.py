from .views         import OrderformView
from django.urls    import path

urlpatterns=[
        path('/orders',OrderformView.as_view()),
        ]
