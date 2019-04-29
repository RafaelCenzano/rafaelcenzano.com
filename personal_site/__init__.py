# Flask imports
from flask import Flask
from flask_mail import Mail
from time import sleep as delay
import threading
import urllib.request

def self_ping():
	while True:
		# 5 minutes delay
		delay(60*5)
		x = urllib.request.urlopen('https://www.rafaelcenzano.me')

ping_self = threading.Thread(target=self_ping, name='self-ping', daemon=True)

ping_self.start()

# Create Flask app
app = Flask(__name__)

# Create Mail app
mail = Mail(app)

# Add Configurations to app
app.config.from_pyfile('config.py', silent=True)

# Import all views
import personal_site.views
