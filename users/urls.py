from django.urls import path

from users.views import (
    FindIdView,UserView,
    FindPasswordView,LoginView,
    SignupCheckView,ReviewView,
    UserLikeView)

urlpatterns = [
    path('/find-id', FindIdView.as_view()),
    path('/signup', UserView.as_view()),
    path('/find-password', FindPasswordView.as_view()),
    path('/signin', LoginView.as_view()),
    path('/signup-check', LoginView.as_view()),
    path('/review/<int:product_id>', ReviewView.as_view()),
    path('/user-like', UserLikeView.as_view())

]
