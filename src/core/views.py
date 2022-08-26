# src/core/views.py

from src.core import bp

@bp.route("/posts")
def hello():
    return "<p class='hello'>Hello, World!</p>"