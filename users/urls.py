from django.urls import path

from users.views import FindIdView,UserView,FindPasswordView

urlpatterns = [
    path('/findid', FindIdView.as_view()),
    path('/signup', UserView.as_view()),
    path('/find-password', FindPasswordView.as_view())
]
