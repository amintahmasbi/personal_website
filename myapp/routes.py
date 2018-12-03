"""route rules for flask
"""

from flask import render_template
from myapp import app

@app.route('/')
@app.route('/index')
def index():
    """redirect index url call to index.html"""
    title = 'My website'
    return render_template('index.html', title=title)
