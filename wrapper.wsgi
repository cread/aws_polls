import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'aws_polls.settings'

sys.path.append('/var/tmp')
sys.path.append('/var/tmp/aws_polls')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

