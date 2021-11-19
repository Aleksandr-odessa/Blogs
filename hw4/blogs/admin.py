from django.contrib import admin
from .models import Post
from django.db import models


admin.site.register(Post) 


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
