# Views controls the display of web pages

from flask import render_template

from . import app
from .database import session, Entry


@app.route("/")  # Root (default) page to display when landing on web site
def entries():  # Query the database entries of the blog
    entries = session.query(Entry)
    entries = entries.order_by(Entry.datetime.desc())
    entries = entries.all()
    return render_template("entries.html", entries=entries)
