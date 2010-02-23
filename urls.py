#   Copyright 2010 Chris Read <chris.read@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

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
