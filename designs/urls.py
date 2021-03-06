
from django.urls import path

from .views import list_designs, details_design, create_design, delete_design, edit_design, create_post

urlpatterns = [
    path('', list_designs, name="list designs"),
    path('details/<int:pk>', details_design, name='design details'),
    path('create/', create_design, name='create design'),
    path('delete/<int:pk>', delete_design, name='delete design'),
    path('edit/<int:pk>', edit_design, name='edit design'),
    path('comment/<int:pk>', create_post, name='comment design'),

]