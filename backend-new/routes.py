from app import db
from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from email_sender import send_email
from models import User, Phone
from utils import is_valid_cpf, is_valid_email, is_valid_phone_number

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register/phone', methods=['POST'])
@jwt_required()
def register_phone():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    data = request.get_json()

    # Extract phone number from request
    number = data.get('number')

    # Check if phone number is valid
    if not is_valid_phone_number(number):
        return jsonify({'error': 'Invalid phone number'}), 400

    # Check if phone number is already registered
    if Phone.query.filter_by(number=number).first():
        return jsonify({'error': 'Phone number already registered'}), 400

    # Create new phone number for the user
    phone_number = Phone(number=number, user=current_user)
    db.session.add(phone_number)
    db.session.commit()

    return jsonify({'message': 'Phone number registered successfully'}), 201

@user_routes.route('/remove/phone', methods=['POST'])
@jwt_required()
def remove_phone():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    data = request.get_json()

    # Extract phone number from request
    number = data.get('number')

    # Find phone number by number and associated with the current user
    phone_number = Phone.query.filter_by(number=number, user=current_user).first()

    if not phone_number:
        return jsonify({'error': 'Phone number not found'}), 404

    db.session.delete(phone_number)
    db.session.commit()

    return jsonify({'message': 'Phone number removed successfully'}), 200

@user_routes.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    profile_data = {
        'cpf': current_user.cpf,
        'full_name': current_user.full_name,
        'date_of_birth': current_user.date_of_birth.isoformat(),
        'address': current_user.address,
        'email': current_user.email,
        'phone_numbers': [phone.number for phone in current_user.phone_numbers]
    }

    return jsonify(profile_data), 200

@user_routes.route('/profile', methods=['PUT'])
@jwt_required()
def edit_profile():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    data = request.get_json()

    # Extract data to be updated
    full_name = data.get('full_name')
    address = data.get('address')
    password = data.get('password')

    # Update user data
    current_user.full_name = full_name or current_user.full_name
    current_user.address = address or current_user.address
    if password:
        current_user.password = password

    db.session.commit()

    return jsonify({'message': 'Profile updated successfully'}), 200

@user_routes.route('/phone/lost', methods=['POST'])
@jwt_required()
def mark_phone_as_lost():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    data = request.get_json()

    # Extract phone number
    number = data.get('number')

    # Find phone number by number and associated with the current user
    phone_number = Phone.query.filter_by(number=number, user=current_user).first()

    if not phone_number:
        return jsonify({'error': 'Phone number not found'}), 404

    # Mark phone number as lost
    phone_number.is_lost = True
    db.session.commit()

    return jsonify({'message': 'Phone number marked as lost'}), 200

@user_routes.route('/phone/found', methods=['POST'])
def report_found_phone():
    data = request.get_json()

    # Extract phone number
    number = data.get('number')

    # Find phone number by number
    phone_number = Phone.query.filter_by(number=number).first()

    if not phone_number:
        return jsonify({'error': 'Phone number not found'}), 404

    # Retrieve owner's contact information
    owner = phone_number.user
    owner_contact = {
        'full_name': owner.full_name,
        'email': owner.email,
        'address': owner.address,
        'phone_numbers': [phone.number for phone in owner.phone_numbers]
    }

    recipient_email = owner_contact['email']
    subject = 'GPP - Seu telefone foi encontrado!'
    message = f'Seu telefone com o número {number} foi encontrado! Procure a delegacia mais próxima.'

    try:
        send_email(recipient_email, subject, message)
        return jsonify({'owner_contact': owner_contact}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 401

