#!/usr/bin/python
#-*- coding: utf-8 -*-


from .base import *

DEBUG = True


INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

STATIC_URL = '/static/'
