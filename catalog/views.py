from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, Blog


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


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Отзывы о магазине продуктов'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        blog_item = Blog.objects.get(pk=self.kwargs.get('pk'))
        context_data['blog'] = blog_item
        context_data['object_list'] = Blog.objects.filter(id=self.kwargs.get('pk'))
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('first_name', 'last_name', 'avatar', 'content')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.first_name) + '_' + slugify(new_blog.last_name)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('first_name', 'last_name', 'avatar', 'content')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.first_name) + '_' + slugify(new_blog.last_name)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


def toggle_blog(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.publication:
        blog_item.publication = False
    else:
        blog_item.publication = True

    blog_item.save()

    return redirect(reverse_lazy('catalog:blog_list'))
