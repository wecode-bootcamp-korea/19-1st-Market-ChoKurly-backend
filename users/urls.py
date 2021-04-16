from django.urls import path

from users.views import FindIdView

urlpatterns = [
    path('/findid', FindIdView.as_view()),
]