from flask_wtf import Form
from wtforms import TextField, validators, ValidationError, TextAreaField, SubmitField

class ContactForm(Form):
   name = TextField('Your Name',[validators.Required('Please enter your name.')])
   email = TextField('Email',[validators.Required('Please enter your email.'),validators.Email('Please enter your email.')])
   message = TextAreaField('Your Message',[validators.Required('Please enter your message.')])
   submit = SubmitField('Send')
