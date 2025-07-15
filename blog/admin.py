from django.contrib import admin
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published', 'created_at']
    list_filter = ['published']
    search_fields = ['title']