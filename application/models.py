from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()



class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    units = models.CharField(max_length=50, verbose_name='Единицы измерения')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.id} - {self.name}'

class Dessert(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='product', verbose_name='Фото')
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, verbose_name='Категория')
    description = models.CharField(max_length=300, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)


class Pay(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.id} - {self.name}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    date_create = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    pay = models.ForeignKey(Pay, related_name='pay', on_delete=models.CASCADE, null=True, verbose_name='Способ оплаты')
    address = models.CharField(max_length=200, null=True, verbose_name='Адрес')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.client} - {self.date_create} - {self.status}'

class OrderDetail(models.Model):
    order = models.ForeignKey(to=Order, related_name='order_details', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Dessert, related_name='dessert', on_delete=models.CASCADE, verbose_name='Продукт')
    count = models.IntegerField(verbose_name='Количество')
    total_sum = models.DecimalField(null=True, max_digits=20, decimal_places=2, verbose_name='Итоговая сумма')

    class Meta:
        verbose_name = 'Элемент деталей заказа'
        verbose_name_plural = 'Детали заказов'

    def __str__(self):
        return f'{self.product.name} - {self.product.price}р'
