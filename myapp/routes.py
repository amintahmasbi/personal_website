"""route rules for flask
"""
import os
from functools import wraps

import requests

from myapp import app

from flask import send_from_directory, safe_join
from flask import request
from flask import jsonify

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """Handle all static html files from Hugo"""
    file_dir = safe_join(app.config['publishDir'], path)
    return send_from_directory(file_dir, app.config['root_html'])

@app.route('/js/<path:path>')
def send_js(path):
    """Redirect js files from Hugo"""
    file_dir = safe_join(app.config['publishDir'], 'js')
    return send_from_directory(file_dir, path)

@app.route('/css/<path:path>')
def send_css(path):
    """Redirect css files form Hugo"""
    file_dir = safe_join(app.config['publishDir'], 'css')
    return send_from_directory(file_dir, path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    """Redirect font files form Hugo"""
    file_dir = safe_join(app.config['publishDir'], 'fonts')
    return send_from_directory(file_dir, path)

@app.route('/img/<path:path>')
def send_img(path):
    """Redirect image files form Hugo"""
    file_dir = safe_join(app.config['publishDir'], 'img')
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

            res = requests.post("https://www.google.com/recaptcha/api/siteverify",
                                data=data)

            result = res.json()

            request.recaptcha_is_valid = bool(result['success'])

        return func(*args, **kwargs)

    return decorated_function

@app.route("/show_email", methods=['POST'])
@check_recaptcha
def show_email():
    """Handle the email show request"""

    response = None
    my_email = os.environ['MY_EMAIL']

    if request.recaptcha_is_valid:
        response = jsonify({'email': my_email})

    return response




# @app.route('/', methods=['POST'])
# # @check_recaptcha
# def email_modal():
#     print("get called")
            # return render_template('search.html')
