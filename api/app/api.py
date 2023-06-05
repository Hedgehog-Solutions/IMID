from flask import (Blueprint, request, current_app, abort, session, g,
                   current_app)
from flask.json import jsonify

import os.path
import functools

from app.db.populate import populate, create_view, connect
from app.model import User, Version

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
    file_path = os.path.join(current_app.instance_path, 'data.csv')
    request.files['data'].save(file_path)
    populate(host, database, user, password, file_path)


@bp.route('/data/<int:version>')
@login_required
def data(version):
    create_view(current_app.config['DATABASE_HOST'],
                current_app.config['DATABASE_NAME'],
                current_app.config['DATABASE_USER'],
                current_app.config['DATABASE_PASSWORD'], version)

    conn, cursor = connect(current_app.config['DATABASE_HOST'],
                           current_app.config['DATABASE_NAME'],
                           current_app.config['DATABASE_USER'],
                           current_app.config['DATABASE_PASSWORD'])

    cursor.execute('SELECT * FROM variants_view;')

    headers = [{'header': col.name, 'accessor': col.name}
               for col in cursor.description]
    data = [{col.name: value for col, value in zip(cursor.description, row)}
            for row in cursor]

    cursor.close()
    conn.close()

    return jsonify(
        {'headers': headers,
         'data': data}
    )


@bp.route('/versions')
@login_required
def versions():
    vs = Version.query.all()
    return jsonify([{'id': v.id, 'from_date': v.from_date.isoformat()}
                    for v in vs])


@bp.route('/export/<int:version>')
@login_required
def export(version):
    ...


@bp.route('/login', methods=('POST',))
def login():
    match request.json:
        case {'email': str(email), 'password': str(password)}:
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
