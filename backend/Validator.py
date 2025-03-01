import re

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
    if not bool(re.search(r'[A-Z]', password)):
        return 'Password must contain capital letters'
    if not bool(re.search(r'[a-z]', password)):
        return 'Password must contain lowercase letters'
    if not bool(re.search(r'[0-9]', password)):
        return 'Password must contain numbers'
    if not bool(re.search(r'[^A-Za-z0-9\s]', password)):
        return 'Password must contain special characters'
    return None