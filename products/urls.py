from django.urls import path

from products.views import CategoryView,ProductListView,SearchView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/list', ProductListView.as_view()),
    path('/search', SearchView.as_view())
]