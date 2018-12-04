"""route rules for flask
"""

from flask import render_template
from myapp import app
from bs4 import BeautifulSoup
import os
import re

@app.route('/')
@app.route('/index')
def index():
    """redirect index url call to index.html"""
    title = 'My website'
    html = "index.html"
    html_path = os.path.join('myapp','templates',html)
    # Parse html
    soup = None
    with open(html_path, "r+") as html_file:
        soup = BeautifulSoup(html_file, 'html5lib')
        # print(soup.prettify())
        for link in soup.find_all(href=re.compile("\.\/")):
            link['href'] = link['href'].replace("./","templates/",1)
        for src in soup.find_all(src=re.compile("\.\/")):
            src['src'] = src['src'].replace("./","templates/",1)
        for div in soup.find_all("div", class_="page-header-image", style=re.compile("\/img")):
            if 'templates' not in div['style']:
                div['style'] = div['style'].replace("/img","templates/img",1)
    with open(html_path, "w") as html_file:
        html_file.write(str(soup))
    # Find the div with the class "full_name", show text
    # print(soup.find("link", { "rel" : "stylesheet" }).text)
    return render_template(html, title=title)
