# Generated by Django 5.0.3 on 2024-03-20 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Понятный URL')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Отзыв')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Аватар')),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('publication', models.BooleanField(default=True)),
                ('view_count', models.IntegerField(default=0, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['date_create', 'publication', 'view_count'],
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Изображение'),
        ),
    ]
