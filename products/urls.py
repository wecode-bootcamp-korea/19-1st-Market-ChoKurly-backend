from django.urls import path

from products.views import CategoryView,ProductView,ProductDetailView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/product', ProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
]
