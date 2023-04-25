from flask import Flask, jsonify, request
from models.user import User
from models.phone_number import PhoneNumber

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    user = User(name, email, password)
    user.save()
    return jsonify(user.__dict__)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.get_all()
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        data = request.get_json()
        user.name = data['name']
        user.email = data['email']
        user.password = data['password']
        user.update()
        return jsonify(user.__dict__)
    return jsonify({'message': 'User not found'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        user.delete()
        return jsonify({'message': 'User deleted'})
    return jsonify({'message': 'User not found'})

@app.route('/users/<int:user_id>/phone_numbers', methods=['GET'])
def get_phone_numbers(user_id):
    phone_numbers = PhoneNumber.get_all_by_user_id(user_id)
    return jsonify(phone_numbers)

@app.route('/users/<int:user_id>/phone_numbers', methods=['POST'])
def create_phone_number(user_id):
    data = request.get_json()
    phone_number = data['phone_number']
    phone_number_obj = PhoneNumber(user_id, phone_number)
    phone_number_obj.save()
    return jsonify(phone_number_obj.__dict__)

@app.route('/users/<int:user_id>/phone_numbers/<int:phone_number_id>', methods=['DELETE'])
def delete_phone_number(user_id, phone_number_id):
    phone_number = PhoneNumber.get_by_id(phone_number_id)
    if phone_number and phone_number.user_id == user_id:
        phone_number.delete()
        return jsonify({'message': 'Phone number deleted'})
    return jsonify({'message': 'Phone number not found'})

if __name__ == '__main__':
    app.run(debug=True, port = 8080)