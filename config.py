# Import os
import os
import secret

SECRET_KEY = str(os.urandom(64))
WTF_CSRF_ENABLED = True
STATIC_FOLDER = 'static'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'contact@lowelldev.club'
MAIL_PASSWORD = secret.mail
MAIL_USE_TLS = False
MAIL_USE_SSL = True
