"""
Django settings for emailer project on Heroku. Fore more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "{{ secret_key }}"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# AWS keys
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET')

# The region of your bucket, more info:
# http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region
S3DIRECT_REGION = 'us-east-1'

#Duplicated AWS settings for Django boto add-in
BOTO_S3_BUCKET = AWS_STORAGE_BUCKET_NAME
BOTO_BUCKET_LOCATION = S3DIRECT_REGION



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'cat',
    'pdf_generator'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'emailer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'emailer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# Enable Connection Pooling (if desired)
DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# AWS Destinations in the following format:
# {destination_key: (path_or_function, auth_test, [allowed_mime_types], permissions, custom_bucket)}
#
# 'destination_key' is the key to use for the 'dest' attribute on your widget or model field
S3DIRECT_DESTINATIONS = {
    # Allow anybody to upload any MIME type
    'misc': ('uploads/misc',),

    # Allow staff users to upload any MIME type
    'files': ('uploads/files', lambda u: u.is_staff,),

    # Allow anybody to upload jpeg's and png's.
    'imgs': ('uploads/imgs', lambda u: True, ['image/jpeg', 'image/png'],),

    # Allow authenticated users to upload mp4's
    'vids': ('uploads/vids', lambda u: u.is_authenticated(), ['video/mp4'],),

    # Allow anybody to upload any MIME type with a custom name function, eg:
    'custom_filename': (lambda original_filename: 'images/unique.jpg',),

    # Specify a non-default bucket for PDFs
    'pdfs': ('/', lambda u: True, ['application/pdf'], None, 'pdf-bucket',),

    # Allow logged in users to upload any type of file and give it a private acl:
    'private': (
        'uploads/vids',
        lambda u: u.is_authenticated(),
        '*',
        'private'),

    # Allow authenticated users to upload with cache-control for a month and content-disposition set to attachment
    'cached': (
        'uploads/vids',
        lambda u: u.is_authenticated(),
        '*',
        'public-read',
        AWS_STORAGE_BUCKET_NAME,
        'max-age=2592000',
        'attachment')
}
