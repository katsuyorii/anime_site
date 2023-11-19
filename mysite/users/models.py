from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import Anime


class User(AbstractUser):
    image = models.ImageField(verbose_name='URL изображения', upload_to='users_images', null=True, blank=True, default='default.png')


class UserAnimeWatchPlanned(models.Model):
    class Status(models.TextChoices):
        WA = 'wa', 'Просмотрено'
        ZP = 'zp', 'Запланировано'

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    anime = models.ForeignKey(to=Anime, on_delete=models.CASCADE, verbose_name='Аниме')
    status = models.CharField(verbose_name='Статус аниме', max_length=2, choices=Status.choices)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Список аниме пользователя'
        verbose_name_plural = 'Списки аниме пользователя'
