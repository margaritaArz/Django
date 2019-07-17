from django.db import models
from django.contrib.auth.models import AbstractUser

class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(verbose_name='имя категории', max_length=255)
    desc = models.TextField(verbose_name='Описание категории', blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=100)
    description = models.TextField(verbose_name='Описание категории', blank=True, null=True)
    image = models.ImageField(upload_to='products_image', blank=True)
    price = models.DecimalField(verbose_name='цена', decimal_places=2, max_digits=8, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class ShopUser(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    def __str__(self):
        return self.username

