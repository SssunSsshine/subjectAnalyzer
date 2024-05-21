from datetime import datetime

from flask import render_template, request, redirect, flash, url_for
from app.models.website import Website
from app import db
from . import routes_bp


@routes_bp.route("/index", methods=['POST', 'GET'])
@routes_bp.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        name = request.form['name']
        last_crawled = datetime.now()

        website = Website(url=url, name=name, last_crawled=last_crawled)

        try:
            db.session.add(website)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            flash(str(e))
            return redirect(url_for('routes.index'))
    else:
        return render_template("index.html")
