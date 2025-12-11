from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

from db import mongo
from routes.users import users_bp
from routes.pets import pets_bp
from routes.activities import activities_bp

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret')

mongo.init_app(app)

app.register_blueprint(users_bp, url_prefix='/api/v1/users')
app.register_blueprint(pets_bp, url_prefix='/api/v1/pets')
app.register_blueprint(activities_bp, url_prefix='/api/v1/activities')

@app.route('/')
def index():
    return jsonify({ 'message': 'DooDrop API running' })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)