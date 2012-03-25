from django.db import models

class Blog(models.Model):

    date = models.DateField(auto_now_add=True)

    blog_url = models.CharField(max_length=64)
    blog_title = models.CharField(max_length=64)
    blog_post = models.TextField()

    def __unicode__(self):
        return self.blog_title
