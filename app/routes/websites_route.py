from flask import render_template
from app.models.website import Website
from . import routes_bp


@routes_bp.route("/websites")
def websites():
    websites = Website.query.all()
    return render_template("websites.html", websites=websites)