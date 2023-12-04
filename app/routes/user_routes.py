from flask import Blueprint, jsonify, request
from ..models.user import User
from ..schemas.user_schema import UserSchema
from ..controllers import user_controller

user_blueprint = Blueprint('user_blueprint', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    users = user_controller.get_all_users()
    return jsonify(users_schema.dump(users))

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    user_data = user_schema.load(request.json)
    new_user = User(**user_data)
    added_user = user_controller.create_user(new_user)
    return jsonify(user_schema.dump(added_user))

@user_blueprint.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user_data = user_schema.load(request.json, partial=True)
    user_data['id'] = id
    user = User(**user_data)
    updated_user = user_controller.update_user(user)
    return jsonify(user_schema.dump(updated_user))

@user_blueprint.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User(id=id)
    deleted_user = user_controller.delete_user(user)
    return jsonify(user_schema.dump(deleted_user))