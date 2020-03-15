"""
Django settings for synonyms project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from gensim.models import KeyedVectors

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '-(_8xe#!xw*20ll_j74qrp38_b!-al$_dmx$aexl&b=csgq125'

DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'synonyms.access_logger.access_log_middleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'synonyms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'synonyms.wsgi.application'

MODEL_PATH = os.path.join(BASE_DIR, 'data/google_news_model.bin')

MODEL = KeyedVectors.load_word2vec_format(
    MODEL_PATH, binary=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'bare': {
            'format': '%(message)s',
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
        }
    },
    'handlers': {
        'access_file_logger': {
            'class': 'logging.FileHandler',
            'formatter': 'bare',
            'filename': 'access.log'
        },
        'common_file_logger': {
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': 'common.log'
        },
    },
    'loggers': {
        'access_logger': {
            'level': 'INFO',
            'handlers': ['access_file_logger'],
            'propagate': False,
        },
        'common_logger': {
            'level': 'INFO',
            'handlers': ['common_file_logger'],
            'propagate': False
        }
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = []

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
