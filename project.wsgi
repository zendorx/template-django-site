import os
import sys
sys.path = ['/var/www/firstweb'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstweb.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
