from django.urls import path

from users.views import FindIdView, LoginView, UserView

urlpatterns = [
    path('/findid', FindIdView.as_view()),
    path('/signup', UserView.as_view()),
    path('/login', LoginView.as_view())
]
