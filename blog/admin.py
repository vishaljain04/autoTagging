from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title", "text")

admin.site.register(Post, PostAdmin)
