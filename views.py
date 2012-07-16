from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.template import Template, Context
from omg_a_blog.blog.models import Blog
from omg_a_blog.blog.forms import ContactForm
from django.http import Http404

GITHUB = ''.join(["https://s3.amazonaws.com/github/ribbons/",
                  "forkme_right_darkblue_121621.png"])

                    
def index(request):

    print request.path
    
    return render_to_response("base.html",
                              {'githuburl': GITHUB},
                              RequestContext(request))


def bloglist(request):
    db = Blog.objects.exclude(blog_title="about")

    if not len(db):
        raise Http404
    
    return render_to_response("blogmode.html",
                              {'blog': db,
                               'githuburl': GITHUB},
                              RequestContext(request))

def blog_entry(request, blogtitle=None):

    if not blogtitle:
        raise Http404
    
    try:
        db = Blog.objects.get(blog_url=blogtitle)
    except Blog.DoesNotExist:
        raise Http404
    
    return render_to_response("blog.html",
                              {'blog': db,
                               'githuburl': GITHUB},
                              RequestContext(request))
