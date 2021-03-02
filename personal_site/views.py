# Imports
from flask import abort, make_response, render_template, send_file
from jinja2.exceptions import TemplateNotFound

from personal_site import app

"""
Views
"""


@app.route("/", methods=["GET"])
def index():
    return render_template("flask_index.html")


@app.route("/apjava", methods=["GET"])
def apjava():
    return render_template("apjava.html")


@app.route("/apjava/<project>", methods=["GET"])
def projects(project):
    try:
        return render_template(f"apjava/{project.lower()}.html")
    except TemplateNotFound as e:
        abort(404)


@app.route("/marvin", methods=["GET"])
def marvin():
    return render_template("marvin.html")


"""
SEO
"""


@app.route("/robots.txt", methods=["GET"])
def robots():
    return send_file("templates/seo/robots.txt")


@app.route("/sitemap.xml", methods=["GET"])
def sitemap():
    sitemap_xml = render_template("seo/sitemap.xml")
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response


"""
Error Handelers
"""


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
