"""
Creates the app and encrypts startup using secret key defined in User enviornment variables

"""

from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    secret_key = os.getenv('WEB_KEY')
    app.config['SECRET_KEY'] = secret_key

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    

    return app