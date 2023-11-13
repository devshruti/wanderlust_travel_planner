from flask import Blueprint, jsonify, request
from app.models import Destination, db

destination_bp = Blueprint('destination_bp', __name__)

@destination_bp.route('/', methods=['GET'])
def home():
    return 'Welcome to Wanderlust Travel Planner'

@destination_bp.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([destination.serialize() for destination in destinations])

@destination_bp.route('/destination/add', methods=['POST'])
def add_destination():
    data = request.get_json()
    new_destination = Destination(name=data['name'], description=data['description'], location=data['location'],
                                 date=data['date'], budget=data['budget'], ratings=data['ratings'])
    db.session.add(new_destination)
    db.session.commit()
    return jsonify({'message': 'Destination added successfully'})

# Similar functions for updating and deleting destinations
