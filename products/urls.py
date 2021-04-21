from django.urls import path

<<<<<<< HEAD
from products.views import CategoryView,ProductView,ProductDetailView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/product', ProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
]
=======
from products.views import CategoryView,ProductListView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/list', ProductListView.as_view()),
]
>>>>>>> main
