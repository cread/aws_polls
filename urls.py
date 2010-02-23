from django.conf.urls.defaults import *

from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

def index(request):
    return HttpResponse("<html><head><title>Simple AWS Polls</title></head><body><h1><center>Simple AWS Polls</center></h1></body></html>")

urlpatterns = patterns('',
    # Example:
    # (r'^aws_polls/', include('aws_polls.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    (r'^admin/(.*)', admin.site.root),
    (r'^polls/', include('aws_polls.polls.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^status$', 'aws_polls.views.status'),
    (r'^$', 'aws_polls.views.index'),
)
