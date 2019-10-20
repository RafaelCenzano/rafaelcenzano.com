# Imports
from personal_site import app
from flask import render_template, request, make_response, redirect, session, url_for, send_file

'''
Views
'''
@app.route("/", methods=['GET'])
def index():
    return render_template('flask_index.py')


@app.route("/404", methods=['GET'])
def notFoundError():
    return render_template('404.py'), 404


@app.route("/500", methods=['GET'])
def serverError():
    return render_template('500.py'), 500

'''
SEO
'''
@app.route('/robots.txt', methods=['GET'])
def robots():
    return send_file('templates/seo/robots.txt')


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    sitemap_xml = render_template('seo/sitemap.xml')
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response

'''
Error Handelers
'''
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('notFoundError'))


@app.errorhandler(500)
def server_error(e):
    return redirect(url_for('serverError'))
