from django.contrib.auth.models import User
from django.db import models


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sent_at']
        indexes = [
            models.Index(fields=['sent_at'])
        ]

    def __str__(self):
        return self.message

