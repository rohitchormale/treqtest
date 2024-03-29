"""
App init module

@author: 
"""

from flask import Flask, redirect, url_for, render_template
import logging
import logging.handlers
from .extensions import *

from .routes import *


def create_app():
    app = Flask(__name__, instance_relative_config=True, template_folder="ui/templates", static_folder="ui/static")
    app.config.from_pyfile("config.py")

    # logging
    handler = logging.handlers.RotatingFileHandler(app.config["LOG_FILE"], maxBytes=app.config["LOG_SIZE"])
    handler.setLevel(app.config["LOG_LEVEL"])
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s [%(pathname)s at %(lineno)s]: %(message)s", "%Y-%m-%d %H:%M:%S"))
    app.logger.addHandler(handler)

    # init extensions
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        # TODO - register blueprints here. e.g.
        # from .routes import auth_blueprint
        # app.register_blueprint(auth_blueprint)
        from .routes import test_blueprint
        app.register_blueprint(test_blueprint)
        csrf.exempt(test_blueprint)


        # TODO register commands here e.g.
        from .commands import txtest_cli
        app.cli.add_command(txtest_cli)


        # finally create tables as per models
        db.create_all()

        @app.route("/")
        def index():
            # TODO - add here endpoint of resource where you want to land on page load. e.g.
            # return redirect(url_for("auth_blueprint.home"))
            return render_template("index.html")

    return app
