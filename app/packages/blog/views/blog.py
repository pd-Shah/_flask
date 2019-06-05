from flask import (
    Blueprint,
    render_template,
)

bp = Blueprint(
    name="blog",
    import_name=__name__,
    template_folder="templates",
    url_prefix="/blog",
    root_path="app/packages/blog",
)


@bp.route("/index")
def index():
    user = { "username": "pd" }
    posts = [
        {
            "author": "pd",
            "body":" HEY Body!",
        },
        {
            "author": "pd",
            "body":"new blog",
        },
        {
            "author": "asghar",
            "body": "HELloO",
        },
    ]
    return render_template(
                "blog/index.html",
                posts=posts,
                user=user,
            )
