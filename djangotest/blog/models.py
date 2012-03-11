from django.db import models

class Blog(models.Model):

    date = models.DateField(auto_now_add=True)
    blog_title = models.CharField(max_length=64)
    blog_post = models.TextField()