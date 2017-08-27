# Views controls the display of web pages

from flask import render_template, request, redirect, url_for

from . import app
from .database import session, Entry


PAGINATE_BY = 10    # Number of entries per page


@app.route("/") # Root (default) page to display when landing on web site
@app.route("/page/<int:page>")  # Specific site page
def entries(page=1):     # Query the database entries of the blog
    # Zero-indexed page
    page_index = page - 1

    count = session.query(Entry).count()

    start = page_index * PAGINATE_BY  # Index of first entry on page
    end = start + PAGINATE_BY  # Index of last entry on page
    total_pages = (count - 1) // PAGINATE_BY + 1  # Total number of pages
    has_next = page_index < total_pages - 1  # Does following page exit?
    has_prev = page_index > 0  # Does previous page exist?

    entries = session.query(Entry)
    entries = entries.order_by(Entry.datetime.desc())
    entries = entries[start:end]

    return render_template("entries.html",
                           entries=entries,
                           has_next=has_next,
                           has_prev=has_prev,
                           page=page,
                           total_pages=total_pages
                           )


@app.route("/entry/add", methods=["GET"])  # Display the blog entry form
def add_entry_get():
    return render_template("add_entry.html")


@app.route("/entry/add", methods=["POST"])  # Take entry form data and put in DB
def add_entry_post():
    entry = Entry(
        title=request.form["title"],
        content=request.form["content"],
    )
    session.add(entry)
    session.commit()
    return redirect(url_for("entries"))
