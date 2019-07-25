from django.urls import path

from .views import basket, basket_add, basket_remove

app_name = 'basketapp'


urlpatterns = [
    path('', basket, name='read'),
    path('basket_add/<int:product_pk>/', basket_add, name='add'),
    path('basket_remove/<int:product_pk>', basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basket.basket_edit, name='edit')
]

