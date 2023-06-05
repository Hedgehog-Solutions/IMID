from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    email = db.Column('email', db.String, primary_key=True)
    _password = db.Column('password', db.String)

    @property
    def password(self):
        raise AttributeError("Can't read password!")

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._password, password)


class Version(db.Model):
    __tablename__ = 'versions'
    id = db.Column('version_id', db.Integer, primary_key=True)
    from_date = db.Column('from_date', db.DateTime, nullable=False)
