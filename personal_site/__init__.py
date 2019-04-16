# Flask imports
from flask import Flask
from flask_mail import Mail

# Create Flask app
app = Flask(__name__)

# Create Mail app
mail = Mail(app)

# Add Configurations to app
app.config.from_pyfile('config.py', silent=True)

# Import all views
import personal_site.views
