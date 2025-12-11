from flask import Blueprint, request, jsonify, current_app
from db import mongo
from bson import ObjectId
from auth import token_required

pets_bp = Blueprint('pets', __name__)

@pets_bp.route('/', methods=['POST'])
@token_required
def create_pet():
    body = request.json or {}
    pet = {
        'owner_id': ObjectId(request.current_user['_id']),
        'name': body.get('name'),
        'species': body.get('species','dog'),
        'breed': body.get('breed',''),
        'age': body.get('age', None),
        'notes': body.get('notes',''),
        'caretakers': [],
        'created_at': datetime.datetime.utcnow()
    }
    res = mongo.db.pets.insert_one(pet)
    return jsonify({'pet_id': str(res.inserted_id)}), 201

@pets_bp.route('/<pet_id>')
@token_required
def get_pet(pet_id):
    pet = mongo.db.pets.find_one({'_id': ObjectId(pet_id)})
    if not pet:
        return jsonify({'message':'not found'}), 404
    pet['id'] = str(pet['_id'])
    pet['owner_id'] = str(pet['owner_id'])
    return jsonify(pet)