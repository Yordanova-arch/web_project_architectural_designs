from django.urls import path

from common.views import main_page, about_page

urlpatterns = [
    path('', main_page, name='index'),
    path('about/', about_page, name='about page'),
]
