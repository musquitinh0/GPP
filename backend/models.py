from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone_numbers = db.relationship('PhoneNumber', backref='user', cascade='all, delete-orphan')

    def __init__(self, cpf, full_name, date_of_birth, address, email, password):
        self.cpf = cpf
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.email = email
        self.password = password


class PhoneNumber(db.Model):
    __tablename__ = 'phone_numbers'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)
    user_cpf = db.Column(db.String(11), db.ForeignKey('users.cpf'), nullable=False)

    def __init__(self, number, user_cpf):
        self.number = number
        self.user_cpf = user_cpf
