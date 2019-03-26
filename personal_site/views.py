from personal_site import app, mail
from json import load, dump
from flask import render_template, request, make_response, redirect, session, url_for, send_file
from personal_site.forms import ContactForm
from flask_mail import Message

# Views
@app.route("/", methods=['GET'])
def index():
    return render_template('flask_index.py')

@app.route("/contact/", methods=['GET','POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.py', form=form)
        else:
            name = form.name.data
            email = form.email.data
            message = form.message.data

            msg = Message('Hello', sender = 'RafaelCenzanoNoReply <contact@lowelldev.club>', recipients = [email])
            msg.body = "Hello Flask message sent from Flask-Mail"
            mail.send(msg)

            return render_template('success.py')
    elif request.method == 'GET':
        return render_template('contact.py', form=form)

@app.route("/404", methods=['GET'])
def error_404():
    return render_template('404.py'), 404

@app.route("/500", methods=['GET'])
def server_error():
    return render_template('500.py'), 500

# SEO
@app.route('/robots.txt', methods=['GET'])
def robots():
    return send_file('templates/seo/robots.txt')

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    sitemap_xml = render_template('seo/sitemap.xml')
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response

# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('error_404'))

# Error Handelers
@app.errorhandler(500)
def server_error(e):
    return redirect(url_for('server_error'))
