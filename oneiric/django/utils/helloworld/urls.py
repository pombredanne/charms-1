from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {"template": "index.html"}),
)
