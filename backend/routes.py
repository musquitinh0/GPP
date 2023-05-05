from flask import Blueprint, request, jsonify
from app import db
from models import User, PhoneNumber

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    cpf = data.get('cpf')
    full_name = data.get('full_name')
    date_of_birth = data.get('date_of_birth')
    address = data.get('address')
    email = data.get('email')
    password = data.get('password')

    new_user = User(cpf=cpf, full_name=full_name, date_of_birth=date_of_birth, address=address, email=email,
                    password=password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@user_routes.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = []
    for user in users:
        user_data = {
            'cpf': user.cpf,
            'full_name': user.full_name,
            'date_of_birth': str(user.date_of_birth),
            'address': user.address,
            'email': user.email,
            'password': user.password
        }
        result.append(user_data)
    return jsonify(result), 200


@user_routes.route('/users/<cpf>', methods=['GET'])
def get_user(cpf):
    user = User.query.filter_by(cpf=cpf).first()
    if user:
        user_data = {
            'cpf': user.cpf,
            'full_name': user.full_name,
            'date_of_birth': str(user.date_of_birth),
            'address': user.address,
            'email': user.email,
            'password': user.password
        }
        return jsonify(user_data), 200
    else:
        return jsonify({'message': 'User not found'}), 404


@user_routes.route('/users/<cpf>', methods=['PUT'])
def update_user(cpf):
    user = User.query.filter_by(cpf=cpf).first()
    if user:
        data = request.get_json()
        user.full_name = data.get('full_name', user.full_name)
        user.date_of_birth = data.get('date_of_birth', user.date_of_birth)
        user.address = data.get('address', user.address)
        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)

        try:
            db.session.commit()
            return jsonify({'message': 'User updated successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'message': 'User not found'}), 404


@user_routes.route('/users/<cpf>', methods=['DELETE'])
def delete_user(cpf):
    user = User.query.filter_by(cpf=cpf).first()
    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'message': 'User not found'}), 404


@user_routes.route('/users/<cpf>/phone_numbers', methods=['POST'])
def add_phone_number(cpf):
    user = User.query.filter_by(cpf=cpf).first()
    if user:
        data = request.get_json()
        number = data.get('number')

        new_phone_number = PhoneNumber(number=number, user_cpf=cpf)

        try:
            db.session.add(new_phone_number)
            db.session.commit()
            return jsonify({'message': 'Phone number added successfully'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'message': 'User not found'}), 404


@user_routes.route('/users/<cpf>/phone_numbers', methods=['GET'])
def get_phone_numbers(cpf):
    user = User.query.filter_by(cpf=cpf).first()
    if user:
        phone_numbers = PhoneNumber.query.filter_by(user_cpf=cpf).all()
        result = []
        for phone_number in phone_numbers:
            phone_number_data = {
                'number': phone_number.number
            }
            result.append(phone_number_data)
        return jsonify(result), 200
    else:
        return jsonify({'message': 'User not found'}), 404


@user_routes.route('/users/<cpf>/phone_numbers/<phone_number_id>', methods=['DELETE'])
def remove_phone_number(cpf, phone_number_id):
    user = User.query.filter_by(cpf=cpf).first()
    if user:
        phone_number = PhoneNumber.query.filter_by(id=phone_number_id, user_cpf=cpf).first()
        if phone_number:
            try:
                db.session.delete(phone_number)
                db.session.commit()
                return jsonify({'message': 'Phone number removed successfully'}), 200
            except Exception as e:
                db.session.rollback()
                return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'message': 'Phone number not found'}), 404
