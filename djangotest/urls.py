from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from djangotest.views import *

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^blog/$', bloglist),
                       url(r'^blog/(.+)/$', blogentry),
                       url(r'^admin/', include(admin.site.urls)),
                       )
