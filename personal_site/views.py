# Imports
from personal_site import app
from flask import render_template, make_response, url_for, send_file

'''
Views
'''


@app.route('/', methods=['GET'])
def index():
    return render_template('flask_index.py')

@app.route('/apjava', methods=['GET'])
def apjava():
    return render_template('apjava.py')

@app.route('/apjava/<project>', methods=['GET'])
def projects(project):
    return render_template(f'apjava/{project.lower()}.py')

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
    return render_template('404.py'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.py'), 500
