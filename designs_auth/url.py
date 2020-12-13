from django.urls import path

from designs_auth.views import LogOutView, LogInView, RegisterView, UserProfileView
from .receivers import *

urlpatterns = [
    path('login/', LogInView.as_view(), name="login user"),
    path('logout/', LogOutView.as_view(), name="logout user"),
    path('register/', RegisterView.as_view(), name='register user'),
    # path('profile/', MyProfile.as_view(), name='my profile'),
    path('profile/', UserProfileView.as_view(), name='my_profile'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
]
