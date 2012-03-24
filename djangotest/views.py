from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.template import Template, Context
from djangotest.blog.models import Blog
from djangotest.blog.forms import ContactForm
from django.http import Http404

GITHUB = ''.join(["https://a248.e.akamai.net/assets.github.com/img/7afbc8b248",
                  "c68eb468279e8c17986ad46549fb71/687474703a2f2f73332e616d617",
                  "a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726",
                  "b6d655f72696768745f6461726b626c75655f3132313632312e706e67"])

import datetime
import subprocess

def index(request):

    print request.path
    
    return render_to_response("base.html",
                              {'githuburl': GITHUB},
                              RequestContext(request))


def bloglist(request):
    db = Blog.objects.exclude(blog_title="about")
    return render_to_response("blogmode.html",
                              {'blog': db,
                               'githuburl': GITHUB},
                              RequestContext(request))

def blog_entry(request, blogtitle=None):

    if not blogtitle:
        raise Http404
    
    try:
        db = Blog.objects.get(blog_title=blogtitle)
    except Blog.DoesNotExist:
        raise Http404
    
    return render_to_response("blog.html",
                              {'blog': db,
                               'githuburl': GITHUB},
                              RequestContext(request))
