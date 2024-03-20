from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Магазин продуктов'
    }


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }


class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['product'] = product_item
        context_data['object_list'] = Product.objects.filter(id=self.kwargs.get('pk'))
        return context_data
