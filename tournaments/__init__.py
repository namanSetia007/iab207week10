from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    from .views import main
    app.register_blueprint(main)
    
    return app