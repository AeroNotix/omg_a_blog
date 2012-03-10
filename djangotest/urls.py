from django.conf.urls.defaults import patterns, include, url

from djangotest.views import *

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^time/(\d{1,2})/$', get_time),
)
