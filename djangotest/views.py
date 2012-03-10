from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.template import Template, Context

import datetime

def index(request):

    return HttpResponse("Hello world")

def get_time(request, time_diff):

    offset = int(time_diff)
    time_diff = datetime.datetime.now() + datetime.timedelta(hours=int(time_diff))
    
    template = Template('''
                        in {{ offset }} {{ hour_word }} the time will be
                        {{time_diff }}
                        ''')

    context = Context(
        {
        'offset': offset,
        'time_diff': time_diff
        }
    )
    
    if offset > 1:
        context['hour_word'] = 'hours'
    else:
        context['hour_word'] = 'hour'

    return HttpResponse(template.render(context))
    
                      
