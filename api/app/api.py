from flask import Blueprint, request, current_app, abort
from flask.json import jsonify

import os.path

from app.db.populate import populate
from app.db.create import create


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/upload', methods=('POST',))
def upload():
    if 'data' not in request.files:
        abort(400)
    db_path = os.path.join(current_app.instance_path, 'test.db')
    if not os.path.exists(db_path):
        create(db_path)
    file_path = os.path.join(current_app.instance_path, 'data.csv')
    request.files['data'].save(file_path)
    populate(db_path, file_path)
    return "Ok"
    # TODO: reszta odpowiedzi


@bp.route('/data/{version:str}')
def data(version):
    return jsonify(
        {'headers': [{'header':'Header Chandler', 'accessor':'red'},
                     {'header':'Header McNamara', 'accessor':'yellow'},
                     {'header':'Header Duke', 'accessor':'green'}],
         'data': [{'red': 21, 'yellow': 37, 'green': 'JP2'},
                  {'red': 14, 'yellow': 88, 'green': 'HH'},
                  {'red': 69, 'yellow': 420, 'green': 'now laugh'}]}
    )


@bp.route('/versions')
def versions():
    ...


@bp.route('/export/{version:str}')
def export(version):
    ...


@bp.route('/login', methods=('POST',))
def login():
    ...


@bp.route('/logout', methods=('POST',))
def logout():
    ...
