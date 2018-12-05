"""
This application runs the back-end of the data project in my portfolio.
"""

from flask import Flask

app = Flask(__name__)
app.config['publishDir'] = 'templates/'
app.config['root_html'] = 'index.html'

from myapp import routes
