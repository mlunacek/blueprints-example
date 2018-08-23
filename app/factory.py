import logging
import json
import os
import time
import copy

from flask import current_app, Flask, redirect, url_for, render_template, jsonify, request

def create_app():
    app = Flask(__name__)

    # Register the admin service blueprint.
    from . public import public
    app.register_blueprint(public, url_prefix='')

    # Register the admin service blueprint.
    from .admin import admin
    app.register_blueprint(admin, url_prefix='/admin')
  
    return app

app = create_app()
