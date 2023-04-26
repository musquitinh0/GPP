from flask import Blueprint, jsonify
from app import db
from models import User, PhoneNumber

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    user_list = []

    for user in users:
        user_dict = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password,
            'phone_numbers': [phone_number.number for phone_number in user.phone_numbers]
        }
        user_list.append(user_dict)

    return jsonify(user_list)


@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    if user is None:
        return jsonify({'message': 'User not found'}), 404

    user_dict = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'password': user.password,
        'phone_numbers': [phone_number.number for phone_number in user.phone_numbers]
    }

    return jsonify(user_dict)


@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    user = User.query.get(user_id)

    if user is None:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()

    user.name = data.get('name')
    user.email = data.get('email')
    user.password = data.get('password')

    db.session.commit()

    return jsonify({'message': 'User updated successfully'})


@user_routes.route('/users/<int:user_id>/phone_numbers', methods=['GET'])
def get_user_phone_numbers(user_id):
    user = User.query.get(user_id)

    if user is None:
        return jsonify({'message': 'User not found'}), 404

    phone_numbers = [phone_number.number for phone_number in user.phone_numbers]

    return jsonify(phone_numbers)


@user_routes.route('/users/<int:user_id>/phone_numbers', methods=['POST'])
def add_user_phone_number(user_id):
    user = User.query.get(user_id)

    if user is None:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()

    number = data.get('number')
    phone_number = PhoneNumber(number=number, user=user)
    db.session.add(phone_number)
    db.session.commit()

    return jsonify({'message': 'Phone number added successfully'})


@user_routes.route('/users/<int:user_id>/phone_numbers/<int:phone_number_id>', methods=['DELETE'])
def remove_user_phone_number(user_id, phone_number_id):
    user = User.query.get(user_id)

    if user is None:
        return jsonify({'message': 'User not found'}), 404

    phone_number = PhoneNumber.query.get(phone_number_id)

    if phone_number is None or phone_number.user != user:
        return jsonify({'message': 'Phone number not found'}), 404

    db.session.delete(phone_number)
    db.session.commit()

    return jsonify({'message': 'Phone number removed successfully'})
