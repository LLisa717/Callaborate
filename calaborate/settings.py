#!/usr/bin/env python
import os
import dj_database_url

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
    from settings.local import *
elif group == 'staging':
    from settings.staging import *
elif group == 'production':
    from settings.production import *
else:
    raise ImproperlyConfigured('DJANGO_SETTINGS_GROUP env var must be set to either "local", "staging", or "production"')

