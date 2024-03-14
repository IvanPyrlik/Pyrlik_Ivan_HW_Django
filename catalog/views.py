from django.shortcuts import render

from catalog.models import Product


def products(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Магазин продуктов'
    }
    return render(request, 'catalog/products.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Ваше {name}, ваш телефон {phone}, ваше сообщение {message}')
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': f'{product_item.name}'
    }
    return render(request, 'catalog/product.html', context)
