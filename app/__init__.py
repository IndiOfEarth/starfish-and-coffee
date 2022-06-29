# PACKAGE STRUCTURE
# package is called app
# all imports are 'from app import'
# models.py contains db Models - Imported here
# routes.py contains all routes
# config.py sets Flask app configuration variables
# __init__.py starts the Flask app and brings everything together
# static and templates folders are all located here

# set persistent env variables using setx NAME "BLAH"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config, DevelopmentConfig, ProductionConfig

# Flask Initialisation
app = Flask(__name__)

# Setting FLASK_ENV and Config
# USE: set FLASK_ENV=development or production BEFORE "flask run"
if app.config["ENV"] == "production":
    app.config.from_object("app.config.ProductionConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("app.config.DevelopmentConfig")


# Flask Extensions
db = SQLAlchemy(app)

# All imports are here
from app import routes
from app import models

