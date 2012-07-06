from omg_a_blog.blog.models import Blog
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
