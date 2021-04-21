from django.urls import path

from users.views import FindIdView,UserView,FindPasswordView,LoginView

urlpatterns = [
    path('/find-id', FindIdView.as_view()),
    path('/signup', UserView.as_view()),
    path('/find-password', FindPasswordView.as_view()),
    path('/signin', LoginView.as_view()),
]
