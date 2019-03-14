from personal_site import app
from json import load, dump # parse and add json data
import urllib.request
from flask import render_template, request, make_response, redirect, session, url_for

# Views
@app.route("/", methods=['GET'])
def index():
    return render_template('flask_index.py')

@app.route("/resume", methods=['GET'])
def resume():
    return redirect('resume.py')

@app.route("/contact", methods=['GET','POST'])
def contact():
    return redirect('contact.py')

@app.route("/400", methods=['GET'])
def error_400():
    return render_template('400.py'), 400

@app.route("/404", methods=['GET'])
def error_404():
    return render_template('404.py'), 404

@app.route("/500", methods=['GET'])
def server_error():
    return render_template('500.py'), 500

# Error Handelers
@app.errorhandler(400)
def bad_request(e):
    return redirect(url_for('error_400'))

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('error_404'))

# Error Handelers
@app.errorhandler(500)
def server_error(e):
    return redirect(url_for('error_500'))
