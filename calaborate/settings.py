#!/usr/bin/env python
"""
Django settings for calaborate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a(1!76zaz1c39bmx2g$k5m@0l2w44*7gtlmv1t&af1uqb5@3xp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pipeline',
    'calaborateApp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
SITE_ID = 1
ACCOUNT_ACTIVATION_DAYS = 1 # One-day activation window; 
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.

ROOT_URLCONF = 'calaborate.urls'

WSGI_APPLICATION = 'calaborate.wsgi.application'

VALID_EMAIL_DOMAINS = (    
    'berkeley.edu',    
    'asdf.com',
)

# if DEBUG:
#     from getpass import getpass
#     EMAIL_USE_TLS = True
#     EMAIL_HOST = 'smtp.gmail.com'
#     EMAIL_PORT = 587
#     EMAIL_HOST_USER = 'icesportsforumsocialmedia@gmail.com'
#     EMAIL_HOST_PASSWORD = getpass('gmailpassword:')
#     DEFAULT_FROM_EMAIL = 'callaborate@gmail.com'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

    'heroku' : {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '',
        'PORT': '5432',
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'

PIPELINE_CSS = {
    'fonts': {
        'source_filenames' :(
            'css/fonts.css',
            'font-awesome-4.2.0/css/font-awesome.min.css'
        ),
        'output_filename': 'css/all_fonts.css',
    },
    'calaborate': {
        'source_filenames': (
            'css/bootstrap.min.css',
            'css/bootstrap-extensions.css',
            'css/stylish-portfolio.css',
            'css/cal.css',
        ),
        'output_filename': 'css/calaborate.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'calaborate': {
        'source_filenames': (
          'js/jquery-1.11.0.js',
          'js/bootstrap.min.js',
          'js/landing.js',
        ),
        'output_filename': 'js/callaborate.js',
    }
}


from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

group = get_env_variable('DJANGO_SETTINGS_GROUP')

if group == 'local':
    from settings_groups.local import *
elif group == 'staging':
    from settings_groups.staging import *
elif group == 'production':
    from settings_groups.production import *
else:
    raise ImproperlyConfigured('DJANGO_SETTINGS_GROUP env var must be set to either "local", "staging", or "production"')

