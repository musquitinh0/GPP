import re

def is_valid_cpf(cpf):
    # TODO
    return True

def is_valid_email(email):
    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return True
    return False

def is_valid_phone_number(number):
    # TODO
    return True
