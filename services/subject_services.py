import db_session 
from models.subject import Subject

def create_subject(name, description, user):

    s = Subject()
    s.name = name
    s.description = description
    s.user_id = user.id

    session = db_session.create_session() 
    session.add(s)
    session.commit()

    return s

def get_subject_by_id(s_id):
    session = db_session.create_session()
    s = session.query(Subject).filter(Subject.id == s_id).first()
    return s
