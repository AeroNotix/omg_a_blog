from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from omg_a_blog.views import *

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^blog/$', bloglist),
                       url(r'^blog/(?P<blogtitle>.+)$', blog_entry),
                       url(r'^about/$', blog_entry, {'blogtitle':"about"}),
                       url(r'^admin/', include(admin.site.urls)),
                       )
