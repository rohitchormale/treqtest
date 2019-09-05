"""
This module implements routes.

author: 

"""
from flask import Blueprint
from . import controllers


# e.g blueprint and routes
# auth_blueprint = Blueprint("auth", "auth", url_prefix="/auth")
# auth_blueprint.add_url_rule("register", "register", controllers.register)

test_blueprint = Blueprint("test", "test", url_prefix="/")
test_blueprint.add_url_rule("get", "get", controllers.get)
test_blueprint.add_url_rule("post", "post", controllers.post, methods=["POST",])


