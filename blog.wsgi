import os
import sys

sys.path.append(r'/var/www')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "omg_a_blog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
