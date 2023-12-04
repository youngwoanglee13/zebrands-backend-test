from ..database.db import db
from ..models.user import User
from .auth_controller import hash_password

def get_all_users()->list[User]:
    return db.session.query(User).all()

def get_user(user:User)->User:
    return db.session.query(User).filter(User.id==user.id).first()

def create_user(user:User)->User:
    user.password = hash_password(user.password)
    db.session.add(user)
    db.session.commit()
    return user

def update_user(user:User) -> User:
    upd_user = User.query.get(user.id)
    for key, value in user.__dict__.items():
         if not key.startswith('_'):
            setattr(upd_user, key, value)
    if user.password:
        upd_user.password = hash_password(upd_user.password)        
    db.session.commit()
    return upd_user

def delete_user(user:User)->User:
    del_user = User.query.get(user.id)
    db.session.delete(del_user)
    db.session.commit()
    return del_user