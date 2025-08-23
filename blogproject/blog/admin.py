from django.contrib import admin
from .models import Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=("title","author_name","published","created_at")
    list_filter=("published","created_at")
    search_fields = ("title", "content", "author_name")
    date_hierarchy = "created_at"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=("name","post","created_at","active")
    list_filter=("active","created_at")
    search_fields=("name","body")