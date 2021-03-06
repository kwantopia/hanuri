# Django settings for hanuri project.
import os

PROJECT_ROOT = os.path.abspath(os.path.join(__file__, os.path.pardir, os.path.pardir))

# for Heroku deployments
if 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
  DEBUG = True
else:
  DEBUG = False

if 'DEPLOY' in os.environ and os.environ['DEPLOY'] == 'true':
  DEPLOY = True  # only True if production (for mail settings and https)
else:
  DEPLOY = False

try:
  from hanuri.settings_debug import *
except Exception as e:
  print e

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

ALLOWED_HOSTS = ['127.0.0.1', '.one2gather.org', '.one2gether.net', 'hanuri-staging.herokuapp.com', 'hanuri.herokuapp.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
AWS_PRELOAD_METADATA = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PROJECT_ROOT + '/sitemedia/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = PROJECT_ROOT + '/sitestatic/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
#STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT + '/static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

if DEPLOY:
  # for handling https static file serving
  from boto.s3.connection import OrdinaryCallingFormat
  AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()
else:
  # for static files to serve from http
  AWS_S3_SECURE_URLS = False

# AWS_S3_CUSTOM_DOMAIN = 'our own cname for the s3 bucket'

if DEBUG is False:
  DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
  DEFAULT_S3_PATH = 'media'
  STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
  STATIC_S3_PATH = 'static'

  MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
  MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
  STATIC_ROOT = '/%s/' % STATIC_S3_PATH
  STATIC_URL = '//s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
  ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=ae0++h%17m@r@@cmzbr(pq-dax7tqv99hygky)%2-549^@$_^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hanuri.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'hanuri.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'main',
)

SOUTH_TESTS_MIGRATE = False

#AUTH_PROFILE_MODULE = 'accounts.UserProfile'

#AUTHENTICATION_BACKENDS = (
#    'emailusernames.backends.EmailAuthBackend',
#)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

if DEPLOY:
  # SENDGRID
  EMAIL_HOST = 'smtp.sendgrid.net'
  EMAIL_PORT = 587
  EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
  EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
  EMAIL_USE_TLS = True
  # MAILGUN
  #EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER')
  #EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')  # 587
  #EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN')
  #EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
else:
  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_PORT = 587
  EMAIL_HOST_USER = ''
  EMAIL_HOST_PASSWORD = ''
  EMAIL_USE_TLS = True

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
  from hanuri.settings_local import *
except Exception as e:
  print e
