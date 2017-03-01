#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
████████╗███████╗███████╗████████╗██╗███╗   ██╗ ██████╗    ██████╗ ██╗   ██╗
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝    ██╔══██╗╚██╗ ██╔╝
   ██║   █████╗  ███████╗   ██║   ██║██╔██╗ ██║██║  ███╗   ██████╔╝ ╚████╔╝
   ██║   ██╔══╝  ╚════██║   ██║   ██║██║╚██╗██║██║   ██║   ██╔═══╝   ╚██╔╝
   ██║   ███████╗███████║   ██║   ██║██║ ╚████║╚██████╔╝██╗██║        ██║
   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝        ╚═╝
"""

import os

from .base import *
from .configs.aws_s3 import *
from .configs.celery import *
from .configs.sentry import *

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ['TEST_REDIS_HOST'],
        "PICKLE_VERSION": -1,
        "OPTIONS": {
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['TEST_DB_NAME'],
        'USER': os.environ['TEST_DB_USER'],
        'PASSWORD': os.environ['TEST_DB_PW'],
        'HOST': os.environ['TEST_DB_HOST'],
        'PORT': os.environ['TEST_DB_PORT'],
    },
}

DEBUG = False

#AWS_S3_CONFIG
AWS_STORAGE_BUCKET_NAME = "elements_testing"
