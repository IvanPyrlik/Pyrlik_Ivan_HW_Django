from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactTemplateView, ProductDetailView, ProductListView, BlogCreateView, BlogListView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_blog

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('list/', BlogListView.as_view(), name='blog_list'),
    path('catalog/', ContactTemplateView.as_view(), name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('toggle_blog/<int:pk>/publication/', toggle_blog, name='toggle_blog'),
]
