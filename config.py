# Import os
import os

SECRET_KEY = str(os.urandom(64))
WTF_CSRF_ENABLED = True
STATIC_FOLDER = 'static'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'contact@lowelldev.club'
MAIL_PASSWORD = os.environ['FLASK_MAIL_PASSWORD']
MAIL_USE_TLS = False
MAIL_USE_SSL = True
