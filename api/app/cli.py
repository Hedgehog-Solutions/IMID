import click
from flask import current_app
from flask.cli import with_appcontext

from .model import *


@click.command('init-db')
@click.option('--reset/--no-reset', default=False)
@with_appcontext
def init_db(reset):
    if reset:
        print('Resetting the database')
        User.__table__.drop()
    print('Recreating the database')
    db.create_all()


@click.command('add-user')
@click.argument('email')
@click.argument('password')
@with_appcontext
def add_user(email, password):
    old_user = User.query.filter(User.email == email).one_or_none()
    if old_user is not None:
        print('Email is already taken')
        print('Use `change-password <email> <new-password>` instead')
        return
    new_user = User(email=email)
    new_user.password = password
    db.session.add(new_user)
    db.session.commit()
    print('Success')


@click.command('change-password')
@click.argument('email')
@click.argument('new_password')
@with_appcontext
def change_password(email, new_password):
    user = User.query.filter(User.email == email).one_or_none()
    if user is None:
        print('No user with this email!')
        return
    user.password = new_password
    db.session.commit()
    print('Success')


@click.command('delete-user')
@click.argument('email')
@with_appcontext
def delete_user(email):
    user = User.query.filter(User.email == email).one_or_none()
    if user is None:
        print('No user with this email!')
        return
    db.session.delete(user)
    db.session.commit()
    print('Success')
