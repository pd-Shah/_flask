from flask import Flask


def create_app():
    app = Flask(
            import_name=__name__,
            )

    @app.route("/")
    def hello():
        return "hello"

    return app
