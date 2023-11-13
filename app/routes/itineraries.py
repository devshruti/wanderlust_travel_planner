from flask import Blueprint, jsonify, request
from app.models import Itinerary, db

itinerary_bp = Blueprint('itinerary_bp', __name__)

@itinerary_bp.route('/itinerary/<int:destination_id>', methods=['GET'])
def get_itinerary(destination_id):
    # Logic to retrieve itinerary for a specific destination
    # Sample logic:
    itinerary = Itinerary.query.filter_by(destination_id=destination_id).all()
    return jsonify([activity.serialize() for activity in itinerary])

@itinerary_bp.route('/itinerary/add', methods=['POST'])
def add_activity_to_itinerary():
    data = request.get_json()
    new_activity = Itinerary(destination_id=data['destination_id'])  # Adjust with actual field names
    # Set other fields based on data received
    db.session.add(new_activity)
    db.session.commit()
    return jsonify({'message': 'Activity added to itinerary successfully'})

@itinerary_bp.route('/itinerary/update/<int:activity_id>', methods=['PUT'])
def update_activity_in_itinerary(activity_id):
    activity = Itinerary.query.get(activity_id)
    if not activity:
        return jsonify({'message': 'Activity not found'})
    data = request.get_json()
    # Update activity fields based on the data received
    db.session.commit()
    return jsonify({'message': 'Activity updated successfully'})

@itinerary_bp.route('/itinerary/delete/<int:activity_id>', methods=['DELETE'])
def delete_activity_from_itinerary(activity_id):
    activity = Itinerary.query.get(activity_id)
    if not activity:
        return jsonify({'message': 'Activity not found'})
    db.session.delete(activity)
    db.session.commit()
    return jsonify({'message': 'Activity deleted successfully'})
