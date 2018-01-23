from .base import *

DEBUG = False

# herokuにデプロイ予定（これでいい？）
ALLOWED_HOSTS = ['.herokuapp.com', ]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# メールをコンソールに表示する。本番環境では使わない？
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('wat.pm22@gmail.com')
EMAIL_HOST_PASSWORD = config('mugi0822')
EMAIL_USE_TLS = True