from flask import (
    Blueprint,
    render_template,
)

bp = Blueprint(
    name="blog",
    import_name=__name__,
    template_folder="templates",
    url_prefix="/index",
    root_path="app/packages/blog",
)


@bp.route("/")
def hello():
    return "hi"
