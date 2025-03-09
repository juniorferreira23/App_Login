import re

def has_number(string: str) -> bool:
    return bool(re.search(r'[0-9]', string))

def has_special_characters(string: str) -> bool:
    return bool(re.search(r"[^a-zA-Z0-9\s]", string))

def has_capital_letter(string: str) -> bool:
    return bool(re.search(r'[A-Z]', string))

def has_lowercase_letter(string: str) -> bool:
    return bool(re.search(r'[a-z]', string))
    
def full_name_validator(full_name):
    if not full_name:
        return 'Empty full name field'
    if has_number(full_name):
        return 'The full name field cannot contain numbers'    
    if has_special_characters(full_name):
        return 'The full name field cannot contain special characters'    
    words = full_name.strip().split()    
    if len(words) < 2:
        return 'The full name field must contain first and last name'    
    for word in words:
        if len(word) < 4:
            return 'The full name field must contain at least 4 characters each word'
    return None

def email_validator(email: str) -> bool:
    if not email:
        return 'Empty email field'
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not bool(re.match(regex, email)):
        return 'Invalid email format'
    return None

def password_validator(password: str, re_password: str = None) -> str|None:
    if not password:
        return 'Empty passoword field'
    if re_password:
        if not re_password:
            return 'Empty repeat passoword field'
        if password != re_password:
            return 'Different passwords'
    if len(password) < 8:
        return 'The password must have at least 8 digits'
    if not has_capital_letter(password):
        return 'Password must contain capital letters'
    if not has_lowercase_letter(password):
        return 'Password must contain lowercase letters'
    if not has_number(password):
        return 'Password must contain numbers'
    if not has_special_characters(password):
        return 'Password must contain special characters'
    return None

def validate_credentials(username: str, password: str, re_password: str = None):
    validator = email_validator(username)
    if validator:
        return validator
    validator = password_validator(password, re_password)
    if validator:
        return validator
    
def validate_register(full_name: str, username: str, password: str, re_password: str = None):
    validator = full_name_validator(full_name)
    if validator:
        return validator
    validator = email_validator(username)
    if validator:
        return validator
    validator = password_validator(password, re_password)
    if validator:
        return validator