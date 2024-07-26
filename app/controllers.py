from app import db
from app.models import User

def add_user(name, email):
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()

def get_all_users():
    return User.query.all()

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()