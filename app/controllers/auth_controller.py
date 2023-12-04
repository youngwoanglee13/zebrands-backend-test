import bcrypt
from app.models.user import User
from ..database.db import db
from flask_jwt_extended import create_access_token

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def login(user:User) -> str:
    stored_user = db.session.query(User).filter(User.email == user.email).first()
    if stored_user is None or not check_password(user.password, stored_user.password):
        return None
    return create_access_token(identity=stored_user.id)
