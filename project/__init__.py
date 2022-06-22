from flask import Flask


def create_app():
    app = Flask(__name__ , template_folder="template",static_folder="static")
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app 
