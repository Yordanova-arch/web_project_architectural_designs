from django.urls import path

from common.views import main_page

urlpatterns = [
    path('', main_page, name='index'),
]
