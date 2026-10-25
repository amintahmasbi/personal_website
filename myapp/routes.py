"""route rules for flask
"""
import os
from functools import wraps

import requests

from myapp import app

from flask import abort, send_from_directory
from werkzeug.utils import safe_join
from flask import request
from flask import jsonify

def _publish_path(*parts):
    """Join under publishDir, returning 404 for paths that escape it"""
    file_dir = safe_join(app.config['publishDir'], *parts)
    if file_dir is None:
        abort(404)
    return file_dir

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """Handle all static html files from Hugo"""
    file_dir = _publish_path(path)
    return send_from_directory(file_dir, app.config['root_html'])

@app.route('/js/<path:path>')
def send_js(path):
    """Redirect js files from Hugo"""
    file_dir = _publish_path('js')
    return send_from_directory(file_dir, path)

@app.route('/css/<path:path>')
def send_css(path):
    """Redirect css files form Hugo"""
    file_dir = _publish_path('css')
    return send_from_directory(file_dir, path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    """Redirect font files form Hugo"""
    file_dir = _publish_path('fonts')
    return send_from_directory(file_dir, path)

@app.route('/img/<path:path>')
def send_img(path):
    """Redirect image files form Hugo"""
    file_dir = _publish_path('img')
    return send_from_directory(file_dir, path)

@app.route('/static/<path:path>')
def send_files(path):
    """Redirect binary files form Hugo"""
    file_dir = _publish_path('static')
    return send_from_directory(file_dir, path)

def check_recaptcha(func):
    """
    Checks Google  reCAPTCHA.

    :param f: view function
    :return: Function
    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """wrapper function"""
        request.recaptcha_is_valid = None
        private_key = os.environ['RECAPTCHA_PRIVATE_KEY']
        if request.method == 'POST':
            data = {'secret': private_key,
                    'response': request.form.get('g-recaptcha-response'),
                    'remoteip': request.access_route[0]}

            try:
                res = requests.post("https://www.google.com/recaptcha/api/siteverify",
                                    data=data, timeout=10)
                result = res.json()
            except (requests.RequestException, ValueError):
                result = {}

            request.recaptcha_is_valid = bool(result.get('success'))

        return func(*args, **kwargs)

    return decorated_function

@app.route("/show_email", methods=['POST'])
@check_recaptcha
def show_email():
    """Handle the email show request"""

    if not request.recaptcha_is_valid:
        return jsonify({'error': 'CAPTCHA verification failed'}), 400

    return jsonify({'email': os.environ['MY_EMAIL']})
