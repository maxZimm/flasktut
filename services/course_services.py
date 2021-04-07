import db_session
from models.course import Course

def create_course(name, summary, course_url, subject):
    session = db_session.create_session()

    c = Course() 
    c.name = name
    c.summary = summary
    c.course_url = course_url
    c.subject_id = subject.id

    session.add(c)
    session.commit()

    return c

def get_course_by_id(course_id):
    session = db_session.create_session()
    course = session.query(Course).filter(Course.id == course_id).first()

    return course

def get_courses_by_subject(subject):
    session = db_session.create_session()
    courses = session.query(Course).filter(Course.subject_id == subject.id).all()

    return courses
  
def del_course(course_id):
    session = db_session.create_session()
    c = session.query(Course).filter(Course.id == course_id).first()
    s_id = c.subject_id
    session.delete(c)
    session.commit()
    session = db_session.create_session()
    check = session.query(Course).filter(Course.id == course_id).first()
    if not check:
        return s_id
    else:
        return False

def update_course(c_id, form_dat):
    session = db_session.create_session()
    c = session.query(Course).filter(Course.id == c_id).first()
    check = False
    for k, v in form_dat.items():
        if (k,v) not in c._items():
            check = True 

    if check:
        c.name = form_dat.get('name')
        c.summary = form_dat.get('summary')
        c.course_url = form_dat.get('course_url')
        session.commit()
