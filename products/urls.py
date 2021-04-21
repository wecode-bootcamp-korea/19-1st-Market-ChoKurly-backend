from django.urls import path

from products.views import CategoryView,ProductListView,ProductDetailView


urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/list', ProductListView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
]