import os
import os.path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import api


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
    # app.config['SQLALCHEMY_DATABASE_URI'] = \
    #     app.config['SQLALCHEMY_DATABASE_URI'.format(instance=app.instance_path)
    # db.init_app(app)

    # the simplest page
    @app.route('/hello')
    def hello():
        return 'Henlo warld!'

    # pages
    app.register_blueprint(api.bp)

    # commandline arguments
    # app.cli.add_command(init_db)

    return app


app = create_app()
