"""
This application runs the back-end of the data project in my portfolio.
"""

from flask import Flask

app = Flask(__name__, static_folder='templates')

from myapp import routes
