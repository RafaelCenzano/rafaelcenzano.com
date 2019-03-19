# Import os
import os

SECRET_KEY = str(os.urandom(64))
WTF_CSRF_ENABLED = True
STATIC_FOLDER = 'static'
