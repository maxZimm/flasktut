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

def get_all_subjects_user(user):
    session = db_session.create_session()
    subjects = session.query(Subject).filter(Subject.user_id == user.id).all()
    return subjects

def update_subject(subject, name_new, name_prev, desc_new, desc_prev):
    if name_new == name_prev and desc_new == desc_prev:
        return False
    session = db_session.create_session()
    s = session.query(Subject).filter(Subject.id == subject.id).first()
    s.name = name_new
    s.description = desc_new
    session.commit()
    return s

def del_subject(subject): 
    session = db_session.create_session()
    s = session.query(Subject).filter(Subject.id == subject.id).first()
    session.delete(s)
    session.commit()
    session = db_session.create_session()
    try:
        session.query(Subject).filter(Subject.id == subject.id).one()
    except:
        return True
    return False
