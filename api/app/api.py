from flask import Blueprint
from flask.json import jsonify


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/upload')
def upload():
    return "Mock upload success"


@bp.route('/download')
def download():
    return jsonify([{'id': 0, 'value': 'Mock'}, {'id': 1, 'value': 'Download'}])
