import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = "clavesecreta"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/bdflaskcardiel"