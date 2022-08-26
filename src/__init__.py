# src/__init__.py

import os

from flask import Flask


def create_app(script_info=None):
    app = Flask(__name__)
    
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    from src.core import bp as core_blueprint
    app.register_blueprint(core_blueprint)

    return app