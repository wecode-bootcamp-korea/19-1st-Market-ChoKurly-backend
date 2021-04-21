from django.urls import path

from products.views import CategoryView,ProductListView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/list', ProductListView.as_view()),
]