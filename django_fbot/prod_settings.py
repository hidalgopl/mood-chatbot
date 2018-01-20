from .settings import *
import django_heroku

django_heroku.settings(locals())
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
