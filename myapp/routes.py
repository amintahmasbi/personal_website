"""route rules for flask
"""
import requests
import os
from functools import wraps
from flask import request

from myapp import app

from flask import send_from_directory, safe_join
from flask import jsonify

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    dir = safe_join(app.config['publishDir'], path)
    return send_from_directory(dir, app.config['root_html'] )

@app.route('/js/<path:path>')
def send_js(path):
    dir = safe_join(app.config['publishDir'], 'js')
    return send_from_directory(dir, path)

@app.route('/css/<path:path>')
def send_css(path):
    dir = safe_join(app.config['publishDir'], 'css')
    return send_from_directory(dir, path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    dir = safe_join(app.config['publishDir'], 'fonts')
    return send_from_directory(dir, path)

@app.route('/img/<path:path>')
def send_img(path):
    dir = safe_join(app.config['publishDir'], 'img')
    return send_from_directory(dir, path)


def check_recaptcha(f):
    """
    Checks Google  reCAPTCHA.

    :param f: view function
    :return: Function
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        request.recaptcha_is_valid = None
        private_key = os.environ['RECAPTCHA_PRIVATE_KEY']
        if request.method == 'POST':
            data = {
            'secret': private_key,
            'response': request.form.get('g-recaptcha-response'),
            'remoteip': request.access_route[0]
            }

            r = requests.post("https://www.google.com/recaptcha/api/siteverify",
            data=data)

            result = r.json()

            if result['success']:
                request.recaptcha_is_valid = True
            else:
                request.recaptcha_is_valid = False

        return f(*args, **kwargs)

    return decorated_function

@app.route("/show_email", methods=['POST'])
@check_recaptcha
def show_email():
    """Handle the email show request"""
    my_email = os.environ['MY_EMAIL']
    if request.recaptcha_is_valid:
        return jsonify({'email': my_email})




# @app.route('/', methods=['POST'])
# # @check_recaptcha
# def email_modal():
#     print("get called")
            # return render_template('search.html')
