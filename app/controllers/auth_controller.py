from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services.auth_service import AuthService

auth_blueprint = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_blueprint.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = auth_service.authenticate_user(username, password)
    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token, group=user.group.name), 200
    return jsonify({"msg": "Bad username or password"}), 401

@auth_blueprint.route('/register', methods=['POST'])
def register():
    # Implement registration logic
    pass

@auth_blueprint.route('/register_group', methods=['POST'])
def register_group():
    # Implement group registration logic for admins
    pass
