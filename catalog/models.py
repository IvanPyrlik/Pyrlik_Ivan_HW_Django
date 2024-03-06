from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(default='', max_length=100, verbose_name='Наименование')
    description = models.TextField(default='', max_length=300, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(default='', max_length=100, verbose_name='Наименование')
    description = models.TextField(default='', max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, default='', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(default=0, verbose_name='Цена за покупку')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_last_change = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')


    def __str__(self):
        return f'{self.name} {self.description} {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)
