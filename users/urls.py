<<<<<<< HEAD
from .views         import UserView
from django.urls    import path

urlpatterns =[
        path('/signup', UserView.as_view()),
]
=======
from django.urls import path

from users.views import FindIdView

urlpatterns = [
    path('/findid', FindIdView.as_view()),
]
>>>>>>> main
