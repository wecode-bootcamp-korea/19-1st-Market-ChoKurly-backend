from django.urls import path

from users.views import FindIdView, FindPasswordView

urlpatterns = [
    path('/find-id', FindIdView.as_view()),
    path('/find-password',  FindPasswordView.as_view()),
]