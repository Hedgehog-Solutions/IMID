import os
import os.path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import api
from app.model import db
from app.cli import *


def create_app(test_config=None):
    global db
    app = Flask(__name__, instance_relative_config=True)

    # load config and overwrite if testing
    app.config.from_pyfile('config.py', silent=True)
    if test_config is not None:
        app.config.from_mapping(test_config)


    # ensure the instance folder exists
    if not os.path.exists(app.instance_path):
        os.mkdir(app.instance_path)

    # connect to database
    app.config['DATABASE_URI'] = \
        app.config['DATABASE_URI'].format(instance=app.instance_path)
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URI']
    db.init_app(app)

    # the simplest page
    @app.route('/hello')
    def hello():
        return 'Henlo warld!'

    # pages
    app.register_blueprint(api.bp)

    # commandline interface
    app.cli.add_command(init_db)
    app.cli.add_command(add_user)
    app.cli.add_command(change_password)
    app.cli.add_command(delete_user)

    @app.after_request
    def handle_CORS(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    return app


app = create_app()
