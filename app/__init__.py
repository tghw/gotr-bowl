"""
Flask Documentation:       http://flask.pocoo.org/docs/
Jinja2 Documentation:      http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:    http://werkzeug.pocoo.org/documentation/
GAE Python Documentation:  http://code.google.com/appengine/docs/python/

This file creates your application.
"""

from os.path import abspath, dirname, join
import sys

root_dir = abspath(join(dirname(__file__), '..'))
sys.path.insert(0, join(root_dir, 'libs'))

from flask import Flask
from werkzeug_debugger_appengine import get_debugged_app
from views import views
import settings

app = Flask(__name__)
app.config.from_object(settings)
app.register_module(views)
app.secret_key = settings.SECRET_KEY
if app.config.get('DEBUG', False):
    app.debug = True
    app = get_debugged_app(app)

# For export
wsgi = app
