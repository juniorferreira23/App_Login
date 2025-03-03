from models.user_model import db, Users

def get_user_by_username(username: str):
    return db.session.query(Users).filter(Users.username == username).one_or_none()
