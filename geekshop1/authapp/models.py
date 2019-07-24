from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType



class ShopUser(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    def __str__(self):
        return self.username

'''class Permission(models.Model):
    name = models.CharField(_('name'), max_length=255)
    content_type = models.ForeignKey(ContentType)
    condename = models.CharField(_('condename'), max_length=100)
    object= PermissionManager()

class ShopUser.group(models.Model):'''
