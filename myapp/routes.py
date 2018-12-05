"""route rules for flask
"""
from myapp import app

from flask import send_from_directory, safe_join

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
