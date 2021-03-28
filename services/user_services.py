import db_session
from models.user import User
from passlib.handlers.sha2_crypt import sha512_crypt as crypt

def find_user_by_email(email):
    session = db_session.create_session()
    return session.query(User).filter(User.email == email).first()

def create_user(first_name, last_name, email, password):
    if find_user_by_email(email):
        return None

    u = User()
    u.first_name = first_name
    u.last_name = last_name
    u.email = email.lower().strip()
    u.hashed_password = hash_text(password)

    session = db_session.create_session()
    session.add(u)

    session.commit()

    return u

def hash_text(text):
    hash_password = crypt.hash(text, rounds=170201)
    return hash_password

def verify_hash(text, hashed_text):
    return crypt.verify(text, hashed_text)
