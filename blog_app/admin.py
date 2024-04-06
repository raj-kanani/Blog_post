from django.contrib import admin
from .models import *


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "publication_date"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author"]
