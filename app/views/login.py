from flask import Blueprint, jsonify, request, make_response
from app.models.client import UserModel
from flask_login import current_user, login_user, logout_user
import ipdb

bp_login = Blueprint('/login', __name__, url_prefix='/login')
@bp_login.route('', methods=['POST'])
def login():
    auth = request.get_json()

    client = UserModel.query.filter_by(email=auth['email']).first()

    if not client:
        return make_response('Email ou senha incorretos', 404)

    if client:
        if UserModel.verify_password(client, auth['password']):
            login_user(client, remember=True)
            # ipdb.set_trace()
            return jsonify({'message': f'success'})

        else:
            return jsonify({'message': f'Email ou senha incorretos'})

    return make_response('Could not verify!', 401)


bp_logout = Blueprint('/logout', __name__, url_prefix='/logout')
@bp_logout.route('')
def logout():
    logout_user()
    return make_response('Sucess on logout!', 200)







