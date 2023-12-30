import string

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=5000)
    short_body = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=50, unique_for_date='created')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    post_manager = PostManager()

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.lower().translate(str.maketrans('', '', string.punctuation)).replace(' ', '-')
        self.short_body = self.body[:100]
        super().save(args, kwargs)

    def get_absolute_url(self):
        return reverse('post:post_detail',
                       args=[self.created.year, self.created.month, self.created.day, self.slug]
                       )
