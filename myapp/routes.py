"""route rules for flask
"""

form flask import render_template
from myapp import app

@app.route('/')
@app.route('/index')
def index():
    title = 'My website'
    return render_template('index.html', title=title)
