from django.urls import path

from designs_auth.views import LogOutView, LogInView, RegisterView
from .receivers import *

urlpatterns = [
    path('login/', LogInView.as_view(), name="login user"),
    path('logout/', LogOutView.as_view(), name="logout user"),
    path('register/', RegisterView.as_view(), name='register user'),
]
