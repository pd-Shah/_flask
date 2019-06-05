from flask import (
    Flask,
    render_template,
)
from app.packages import blog


def create_app():
    app = Flask(
            import_name=__name__,
            )

    app.register_blueprint(blog.bp)
    return app
