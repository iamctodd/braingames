# For brevity, activities.py includes only create and list endpoints

from flask import Blueprint, request, jsonify
from db import mongo
from bson import ObjectId
from auth import token_required
import datetime

activities_bp = Blueprint('activities', __name__)

@activities_bp.route('/<pet_id>', methods=['POST'])
@token_required
def create_activity(pet_id):
    body = request.json or {}
    act = {
        'pet_id': ObjectId(pet_id),
        'user_id': ObjectId(request.current_user['_id']),
        'type': body.get('type'),
        'subtype': body.get('subtype'),
        'notes': body.get('notes',''),
        'created_at': datetime.datetime.utcnow(),
        'recorded_at': body.get('recorded_at', datetime.datetime.utcnow().isoformat())
    }
    res = mongo.db.activities.insert_one(act)
    return jsonify({'activity_id': str(res.inserted_id)}), 201

@activities_bp.route('/list/<pet_id>')
@token_required
def list_activities(pet_id):
    items = list(mongo.db.activities.find({'pet_id': ObjectId(pet_id)}).sort('created_at', -1).limit(100))
    for it in items:
        it['id'] = str(it['_id'])
        it['pet_id'] = str(it['pet_id'])
        it['user_id'] = str(it['user_id'])
    return jsonify(items)