from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__,template_folder="template")
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app 
