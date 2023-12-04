from flask import Blueprint, jsonify, request
from app.models.user import User
from app.schemas.user_schema import UserSchema
from ..controllers import auth_controller


auth_blueprint = Blueprint('auth_blueprint', __name__)
user_schema = UserSchema()

@auth_blueprint.route('/login', methods=['POST'])
def login():
    user_data = user_schema.load(request.json, partial=True)
    user = User(**user_data)
    token = auth_controller.login(user)
    if token!=None:
        return jsonify(access_token=token)
    return "invalid credentials"