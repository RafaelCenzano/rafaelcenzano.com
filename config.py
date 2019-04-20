# Import os
import os

SECRET_KEY = os.urandom(32)
WTF_CSRF_ENABLED = True
STATIC_FOLDER = 'static'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'contact@lowelldev.club'
MAIL_PASSWORD = os.environ['FLASK_MAIL_PASSWORD']
MAIL_USE_TLS = False
MAIL_USE_SSL = True
WTF_CSRF_SECRET_KEY = os.urandom(32)
