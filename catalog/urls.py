from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, product, products

app_name = CatalogConfig.name

urlpatterns = [
    #path('', home, name='home'),
    path('', products, name='products'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', product, name='product'),
]
