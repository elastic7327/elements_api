#!/usr/bin/python
#-*- coding: utf-8 -*-
"""

██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗   ██████╗ ██╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║   ██╔══██╗╚██╗ ██╔╝
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║   ██████╔╝ ╚████╔╝
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║   ██╔═══╝   ╚██╔╝
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║██╗██║        ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝        ╚═╝

"""
import os

from .base import *
from .configs.aws_s3 import *
from .configs.celery import *
from .configs.sentry import *

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ['PRO_REDIS_HOST'],
        "PICKLE_VERSION": -1,
        "OPTIONS": {
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['PRO_DB_NAME'],
        'USER': os.environ['PRO_DB_USER'],
        'PASSWORD': os.environ['PRO_DB_PW'],
        'HOST': os.environ['PRO_DB_HOST'],
        'PORT': os.environ['PRO_DB_PORT'],
    },
}

DEBUG = False

#AWS_S3 CONFIG
AWS_STORAGE_BUCKET_NAME = "elements_production"
