from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.template.loader import get_template

def index(request):

    return HttpResponse("Hello world")
