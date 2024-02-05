from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += [

    'sslserver', # for running https locally
    'livereload',
]
middlewares = [
    "livereload.middleware.LiveReloadScript",
]

try:
    from .local import *
except ImportError:
    pass
