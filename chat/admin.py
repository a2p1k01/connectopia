from django.contrib import admin

from chat.models import ChatMessage


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'sent_at']
    list_filter = ['sent_at']
    search_fields = ['user', 'message']
