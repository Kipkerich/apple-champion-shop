from django.urls import path, include
from . import views as my_views

urlpatterns = [
    path('', my_views.products, name='products-url'),
    path('add-products/', my_views.add_products, name='add-products-url'),
    path('delete/<id>', my_views.delete, name='delete-url'),
    path('update/<id>', my_views.update_products, name='update-product-url'),
    path('pay/<id>', my_views.pay, name='pay-url')
    ]