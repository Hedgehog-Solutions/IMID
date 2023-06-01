from flask import Blueprint, request, current_app, abort
from flask.json import jsonify

import os.path

from app.db.populate import populate
from app.db.create import create

host="change"
database="change"
user="change"
password="change123"


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/upload', methods=('POST',))
def upload():
    if 'data' not in request.files:
        abort(400)
    db_path = os.path.join(current_app.instance_path, 'test.db')
    # if not os.path.exists(db_path):
    if True:
        create(host, database, user, password) #TODO
    file_path = os.path.join(current_app.instance_path, 'data.csv')
    request.files['data'].save(file_path)
    populate(host, database, user, password, file_path)
    return "Ok"


@bp.route('/download')
def download():
    return jsonify([{'id': 0, 'value': 'Mock'}, {'id': 1, 'value': 'Download'}])
