from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token
from app import db
from models import User
from utils import is_valid_email, is_valid_cpf

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Extract user data from request
    cpf = data.get('cpf')
    full_name = data.get('full_name')
    date_of_birth = data.get('date_of_birth')
    address = data.get('address')
    email = data.get('email')
    password = data.get('password')

    # Check if CPF and email are valid
    if not is_valid_cpf(cpf):
        return jsonify({'error': 'Invalid CPF'}), 400
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email'}), 400

    # Check if CPF and email are already registered
    if User.query.filter_by(cpf=cpf).first():
        return jsonify({'error': 'CPF already registered'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    # Create new user
    user = User(cpf=cpf, full_name=full_name, date_of_birth=date_of_birth,
                address=address, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Extract email and password from request
    email = data.get('email')
    password = data.get('password')

    # Find user by email
    user = User.query.filter_by(email=email).first()

    # Check if user exists and password is correct
    if not user or user.password != password:
        return jsonify({'error': 'Invalid email or password'}), 401

    # Generate access token
    access_token = create_access_token(identity=user.id)

    return jsonify({'access_token': access_token}), 200
