from .base import *
import os

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

DEBUG = True

ALLOWED_HOSTS = ['excoloholdings.herokuapp.com', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["NAME"],
        'USER': os.environ["USER"],
        'PASSWORD': os.environ["PASSWORD"],
        'HOST': os.environ["HOST"],
        'PORT': os.environ["PORT"],
    }
}

db_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_env) 

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

django_heroku.settings(locals())