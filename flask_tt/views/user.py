from flask import Blueprint, request, jsonify, redirect, \
    url_for
from flask_tt.models import User, db
import json

mod = Blueprint('user', __name__, url_prefix='/user')


@mod.route('/<int:id>', methods=['GET'])
def get(id):
    user = User.query.filter(User.id == id).first()
    return jsonify(username=user.user_name, roleName=user.role.role_name, id=id)


@mod.route('/', methods=['POST'])
def add():
    data = json.loads(request.data)
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(username=user.user_name, roleName=user.role.role_name)


@mod.route('/', methods=['DELETE'])
def delete():
    data = json.loads(request.data)
    user = User.query.filter(User.id == data['id']).first()
    db.session.delete(user)
    db.session.commit()
    return 'ok'


@mod.route('/', methods=['PUT'])
def modefiy():
    data = json.loads(request.data)
    user = User.query.filter(User.id == data['id']).first()
    user.role_id = data['id']
    db.session.commit()
    return jsonify(username=user.user_name, roleName=user.role.role_name)


@mod.route('/', methods=['GET'])
def get_for_page():
    data = json.loads(request.data)
    page_index = data['pageIndex']
    page_size = data['pageSize']
    users = User.query.order_by(-User.id).paginate(page_index, page_size)
    result = []
    for user in users.items:
        result.append({'userName': user.user_name, 'roleName': user.role.role_name})
    return jsonify(result)
