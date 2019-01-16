# Imports

# Flask imports
from flask import Flask

# Flask app
app = Flask(__name__)

# Add Configs
app.config.from_pyfile('config.py', silent=True)

import personal_site.views
