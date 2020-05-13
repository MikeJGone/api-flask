from flask import Blueprint, request, jsonify
from flask_tt.models import User, db, Role
from flask_tt.cache import *
import json

mod = Blueprint('user', __name__, url_prefix='/user')


@mod.route('/<int:id>', methods=['GET'])
def get(id):
    key = 'user_id_%s' % str(id)
    role_key = ""
    if not get_cache_data(key):
        user = User.query.filter(User.id == id).first()
        # user 自身的字段序列化缓存
        set_cache_data(key, dict(user))
        role_key = 'role_id_%s' % str(user.role_id)
        # user 相关的role的字段序列化缓存
        set_cache_data(role_key, dict(user.role))
        role = user.role
        print("no cache")
    else:
        user = User(**get_cache_data(key))
        role_key = 'role_id_%s' % str(user.role_id)
        role = Role(**get_cache_data(role_key))
        print("cache")
    return jsonify(username=user.user_name, roleName=role.role_name, id=id)


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
    clean_cache_data('user_id_%s' % user.id)
    clean_cache_datas('user_page')
    return 'ok'


@mod.route('/', methods=['PUT'])
def modefiy():
    data = json.loads(request.data)
    user = User.query.filter(User.id == data['id']).first()
    user.role_id = data['role_id']
    db.session.commit()
    clean_cache_data('user_id_%s' % user.id)
    clean_cache_datas('user_page')
    return jsonify(username=user.user_name, roleName=user.role.role_name)


@mod.route('/', methods=['GET'])
def get_for_page():
    data = json.loads(request.data)
    page_index = data.get('pageIndex')
    page_size = data.get('pageSize')
    type = data.get('type', 'id')
    key = f"user_page_{type}_{page_index}_{page_size}"
    result = []
    if not get_cache_data(key):
        users = User.query.order_by(type).paginate(page_index, page_size)
        for user in users.items:
            result.append({'userName': user.user_name, 'roleName': user.role.role_name})
        set_cache_data(key, result)
        print('no cache')
    else:
        result = get_cache_data(key)
        print('cache')
    return jsonify(result)
