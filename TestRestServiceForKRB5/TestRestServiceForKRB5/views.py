"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask_gssapi import GSSAPI
from TestRestServiceForKRB5 import app

gssapi = GSSAPI(app)

@app.route('/')
@app.route('/home')
@gssapi.require_auth()
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
@gssapi.require_auth()
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
@gssapi.require_auth()
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
