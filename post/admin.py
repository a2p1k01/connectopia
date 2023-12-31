from django.contrib import admin
from post.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created']
    list_filter = ['title', 'author', 'created']
    search_fields = ['title', 'author']
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ['author']
    date_hierarchy = 'created'
    ordering = ['title', 'author', 'created']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created']
    list_filter = ['created']
    search_fields = ['user', 'body']
