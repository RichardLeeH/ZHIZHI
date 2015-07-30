# -*- coding: utf-8 -*-
# $ make mail
import os
DEBUG = False
SQLALCHEMY_ECHO = False
SECRET_KEY = 'nfewqf0-9jv0sa90f23rr135490jk89jo0fdasldsafd'

LOG_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

STATIC_FOLDER = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), 'static')
UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), 'media')
UPLOAD_URL = "http://127.0.0.1:5000/wifi/admin"

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'apk'}
ALLOWED_PIC = {'png', 'jpg', 'jpeg'}

# Celery
BROKER_TRANSPORT = 'redis'
CELERY_BROKER_URL = 'redis://192.168.199.8:6379'
CELERY_RESULT_BACKEND = 'redis://192.168.199.8:6379'
CELERY_TASK_SERIALIZER = 'json'
CELERY_DISABLE_RATE_LIMITS = True
CELERY_ACCEPT_CONTENT = ['json', ]

# Auth
SESSION_COOKIE_NAME = 'session'

# SQLALCHEMY 连接池配置
SQLALCHEMY_POOL_SIZE = 200
SQLALCHEMY_MAX_OVERFLOW = 1000
SQLALCHEMY_POOL_TIMEOUT = 10
SQLALCHEMY_POOL_RECYCLE = 80


# cache
CACHE_TYPE = 'redis'
CACHE_REDIS_HOST = '192.168.199.8'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = 16
CACHE_REDIS_TIMEOUT = 15
CACHE_REDIS_URL = 'redis://192.168.199.8:6379'
