from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(verbose_name='URL изображения', upload_to='users_images', null=True, blank=True, default='default.png')