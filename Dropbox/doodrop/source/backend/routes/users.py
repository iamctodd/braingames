from flask import Blueprint, request, jsonify, current_app
from db import mongo
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime

users_bp = Blueprint('users', __name__)
users = lambda: mongo.db.users

@users_bp.route('/register', methods=['POST'])
def register():
    body = request.json or {}
    if not body.get('email') or not body.get('password'):
        return jsonify({'message':'email and password required'}), 400
    if users().find_one({'email': body['email']}):
        return jsonify({'message':'email exists'}), 400
    pw_hash = generate_password_hash(body['password'])
    user = {
        'email': body['email'],
        'password_hash': pw_hash,
        'name': body.get('name',''),
        'account_type': 'owner',
        'created_at': datetime.datetime.utcnow()
    }
    res = users().insert_one(user)
    token = jwt.encode({'user_id': str(res.inserted_id), 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)}, current_app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token, 'user': {'email': user['email'], 'name': user['name']}}), 201

@users_bp.route('/login', methods=['POST'])
def login():
    body = request.json or {}
    user = users().find_one({'email': body.get('email')})
    if not user or not check_password_hash(user['password_hash'], body.get('password','')):
        return jsonify({'message':'invalid credentials'}), 401
    token = jwt.encode({'user_id': str(user['_id']), 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)}, current_app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token, 'user': {'email': user['email'], 'name': user.get('name','')}})

@users_bp.route('/me')
def me():
    # simple example — in production decorate with token_required
    auth = request.headers.get('Authorization')
    if not auth:
        return jsonify({'message':'no token'}), 401
    token = auth.split()[1]
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    user = users().find_one({'_id': mongo.ObjectId(data['user_id'])})
    return jsonify({'email': user['email'], 'name': user.get('name')})