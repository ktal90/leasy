# -*- coding: utf-8 -*-
import os

class Config(object):
    SECRET_KEY = 'shhhh'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://lynmohoiumcrdk:QMO_3j5Bn6S0p90Syi-cMXkcyE@ec2-54-197-241-97.compute-1.amazonaws.com:5432/d5r3k95etc3bhn'
    SQLALCHEMY_ECHO = False

class DevConfig(Config):
    DEBUG = True
    DB_NAME = "test.db"
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}".format(DB_PATH)
    SQLALCHEMY_ECHO = True