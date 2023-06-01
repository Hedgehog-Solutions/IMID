from flask import Blueprint, request, current_app, abort, session, g
from flask.json import jsonify

import os.path
import functools

from app.db.populate import populate
from app.db.create import create
from app.model import User

host="change"
database="change"
user="change"
password="change123"


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.before_app_request
def load_user():
    if 'user_email' in session and session['user_email'] is not None:
        g.user = User.query.get(session['user_email'])
    else:
        g.user = None


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return '', 401
        return view(**kwargs)
    return wrapped_view


@bp.route('/upload', methods=('POST',))
@login_required
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
    # TODO: reszta odpowiedzi


@bp.route('/data/{version:str}')
@login_required
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
@login_required
def versions():
    ...


@bp.route('/export/{version:str}')
@login_required
def export(version):
    ...


@bp.route('/login', methods=('POST',))
def login():
    match request.json:
        case {'username': str(email), 'password': str(password)}:
            user = User.query.filter(User.email == email).one_or_none()
            if user is None or not user.verify_password(password):
                return ('Invalid credentials', 401)
            else:
                session['user_email'] = user.email
                return '', 200
        case _:
            return 'Invalid request', 400


@bp.route('/logout', methods=('POST',))
@login_required
def logout():
    session['user_email'] = None
    return '', 200 
