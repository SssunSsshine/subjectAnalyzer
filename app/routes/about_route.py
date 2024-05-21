from flask import render_template
from . import routes_bp


@routes_bp.route("/about")
def about():
    return render_template("about.html")
