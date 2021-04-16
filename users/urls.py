from django.urls import path

from users.views import FindIdView, FindPwView

urlpatterns = [
    path('/findid', FindIdView.as_view()),
    path('/findpw',  FindPwView.as_view()),
]