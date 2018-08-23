from flask import render_template
from .blueprint import public

@public.route("/")
def index():
    return render_template('index.html')
