from personal_site import app
from json import load, dump # parse and add json data
import urllib.request
from flask import render_template, request, make_response, redirect, session

# Views
@app.route("/", methods=['GET'])
def index():
    return render_template('flask_index.py')

@app.route("/resume", methods=['GET'])
def resume():
    return redirect('https://www.linkedin.com/in/rafael-cenzano/')

@app.route("/contact", methods=['GET','POST'])
def contact():
    return redirect('contact.py')

@app.route("/404", methods=['GET'])
def error_404():
    return render_template('404.py')
