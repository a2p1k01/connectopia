# from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    avatar = models.ImageField(upload_to='images/', default='images/avatar.png')
    status = models.CharField(max_length=100, default='', blank=True)

    # def is_online(self):
    #     return (timezone.now() - self.user.is_authenticated) < timezone.timedelta(minutes=1)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(args, kwargs)
