from flask import Flask

#initializing application
app = Flask(__name__)

#Setting up configuration
app.config.from_objects(DevConfig)

from app import views
