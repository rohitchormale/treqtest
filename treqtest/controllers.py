"""
This module implements webapp controllers.

@author: 
"""

from flask import request, render_template, jsonify, flash
from .models import *
from .extensions import auth


def flash_errors(form):
    """Generate flashes for errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')


# e.g. controllers
# def register():
#     context = {"title": "home"}
#     return render_template("foo.html", **context)
#
# def register_api():
#     return jsonify({"first_name": "foo"}), 200

from werkzeug.security import generate_password_hash, check_password_hash
users = {
    "john": generate_password_hash("john"),
    "jane": generate_password_hash("jane"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@auth.login_required
def get():
    return jsonify({"foo": "bar", "req": "get"})


@auth.login_required
def post():
    return jsonify({"foo": "bar", "req": "post"})
