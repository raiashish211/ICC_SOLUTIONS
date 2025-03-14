from django.urls import path
from .views import item_list,about

urlpatterns = [
    path('', item_list, name='item_list'),
    path('/about', about, name='about'),
    path('products', about, name='products'),
]