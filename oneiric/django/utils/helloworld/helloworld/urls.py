from django.conf.urls.defaults import patterns, url, include
from django.views.generic.simple import direct_to_template
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {"template": "index.html"}),
    url(r'^environ/?$', 'views.hello_world'),
    url(r'^admin/', include(admin.site.urls)),
)
