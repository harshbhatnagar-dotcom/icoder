from django.contrib import admin
from .models import Post, BlogComment




admin.site.register(Post)     # Register Post with Summernote editor
admin.site.register(BlogComment) 



# Register your models here.
