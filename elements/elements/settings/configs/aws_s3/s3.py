
import os

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.environ.get(
    'AWS_ACCESS_KEY',
     os.environ['AWS_ACCESS_KEY'])
AWS_SECRET_ACCESS_KEY = os.environ.get(
    'AWS_SECRET_KEY', os.environ['AWS_SECRET'])
AWS_STORAGE_BUCKET_NAME = ''

# turn off expiration
AWS_QUERYSTRING_AUTH = False
