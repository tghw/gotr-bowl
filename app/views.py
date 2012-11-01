from flask import Module, render_template
from context import context_processors
from decorators import requires_auth, requires_admin

views = Module(__name__, 'views')
views.app_context_processor(context_processors)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/authed')
@requires_auth
def authed():
    return render_template('authed.html')

@views.route('/admin')
@requires_admin
def admin():
    return render_template('admin.html')
