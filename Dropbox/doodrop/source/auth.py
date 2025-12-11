from functools import wraps
from flask import request, jsonify, current_app
import jwt
from db import mongo

users = lambda: mongo.db.users

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        header = request.headers.get('Authorization')
        if not header:
            return jsonify({'message':'Missing token'}), 401
        try:
            token = header.split()[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            user = users().find_one({'_id': mongo.ObjectId(data['user_id'])})
            if not user:
                raise Exception('User not found')
            request.current_user = user
        except Exception as e:
            return jsonify({'message':'Token invalid', 'error': str(e)}), 401
        return f(*args, **kwargs)
    return decorated