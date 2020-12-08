from django.urls import path
from . import views
from .views import list_designs, details_design

urlpatterns = [
    path('', list_designs, name="list designs"),
    path('details/<int:pk>', details_design, name='design details')
]