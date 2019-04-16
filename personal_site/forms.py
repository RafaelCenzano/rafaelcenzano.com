from flask_wtf import FlaskForm
from wtforms import TextField, validators, ValidationError, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
   name = TextField('Your Name', validators=[DataRequired()])
   email = TextField('Email', validators=[DataRequired(),Email()])
   message = TextAreaField('Your Message', validators=[DataRequired()])
