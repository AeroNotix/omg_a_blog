from django.conf.urls.defaults import patterns, include, url

from djangotest.views import *

urlpatterns = patterns('',
    url(r'^$', index),
)
