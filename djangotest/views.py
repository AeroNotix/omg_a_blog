from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.template import Template, Context
from djangotest.blog.models import Blog

from django.http import Http404

import datetime

def index(request):

    return HttpResponse("Hello world")

def bloglist(request):

    db = Blog.objects.all()
    
    return render_to_response("blogmode.html",
                              {'blog': db},
                              RequestContext(request))

def blogentry(request, blog_title):

    try:
        db = Blog.objects.get(blog_title=blog_title)
    except Blog.DoesNotExist:
        raise Http404
    
    return render_to_response("blog.html",
                              {'blog': db},
                              RequestContext(request))
    
                      
