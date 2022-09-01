# Isolating configuration in a separate file from run.py
# A configuration file for the Flask app
import os

class Config():
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///cafes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True  # only sends cookies if running on https
    SECRET_KEY = 'qrtsyTWZaNQPAXsPYQmQ0A'

class ProductionConfig(Config):
    ENV = "production"

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SESSION_COOKIE_SECURE = False

