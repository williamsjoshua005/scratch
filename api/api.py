import json

import peewee
from flask import request

from app import app, db
from db.user import User


@app.route('/users')
def get_all_users():
    users = [user for user in User.select().dicts()]
    return json.dumps(users), {'Content-Type': 'application/json'}


@app.route('/users/<int:user_id>')
def get_user(user_id: int):
    try:
        user = User.get(User.id == user_id)
        return json.dumps(user.dict()), {'Content-Type': 'application/json'}
    except peewee.DoesNotExist:
        return f'user {user_id} does not exist', 400


@app.route('/users', methods=['POST'])
def create_user():
    # if request.data
    body: dict = request.json
    if body is None or len(body) == 0:
        return 'you must add a request body with application/json as content-type', 400

    uid = body['id'] if 'id' in body.keys() else None
    name = body['name'] if 'name' in body.keys() else None

    if uid is None or len(str(uid).strip()) == 0 or name is None or len(str(name).strip()) == 0:
        return 'id or name cannot be empty or null', 400

    if user_exists(uid):
        return f'id {uid} is already present', 400

    User.create(id=uid, name=name)
    return '', 200, {'Content-Type': 'application/json'}


def user_exists(uid) -> bool:
    try:
        User.get_by_id(uid)
        return True
    except peewee.DoesNotExist:
        return False


@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response
