# -*- coding: utf-8 -*-

# from flask.ext.sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
#
# from flask.ext.login import LoginManager
# login_manager = LoginManager()
# login_manager.login_view = 'auth.admin_login'


# from flask.ext.migrate import Migrate
# migrate = Migrate()

from flask.ext.wtf.csrf import CsrfProtect
csrf = CsrfProtect()

from flask.ext.cache import Cache
cache = Cache()

# from celery import Celery
#
# celery = Celery()
