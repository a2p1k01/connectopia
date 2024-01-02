import string, secrets

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='images/', default='', null=True, blank=True)
    slug = models.SlugField(max_length=50, unique_for_date='created')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    post_manager = PostManager()

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = (
            self.title.lower()
            .translate(str.maketrans('', '', string.punctuation))
            .replace(' ', '-') +
            ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(5))
        )
        super().save(args, kwargs)

    def get_absolute_url(self):
        return reverse('post:post_detail',
                       args=[self.created.year, self.created.month, self.created.day, self.slug]
                       )


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return f'Comment by {self.user} to {self.post} on {self.created}'

