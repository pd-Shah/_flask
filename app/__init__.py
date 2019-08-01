from os import mkdir
from flask import (
    Flask,
    render_template,
)
from app.packages import blog
from settings import Setting


def create_app():
    app = Flask(
            import_name=__name__,
            instance_relative_config=True,
            )
    try:
        mkdir(app.instance_path, )
    except Exception as e:
        print(e)
    app.config.from_object(Setting)
    app.config.from_pyfile(filename="settings.py", silent=False)
    app.register_blueprint(blog.bp)
    return app
